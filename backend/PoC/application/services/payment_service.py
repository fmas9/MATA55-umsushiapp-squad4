from datetime import datetime, timezone
from typing import List
from uuid import UUID, uuid4

from application.ports.order_repository_port import OrderRepositoryPort
from application.ports.payment_gateway import PaymentGateway
from application.ports.payment_repository_port import PaymentRepositoryPort
from domain.dtos.payment_create import CreatePaymentDTO
from domain.entities.order import OrderStatus
from domain.entities.payment import Payment
from domain.entities.transaction import Transaction
from enums.payment_type import PaymentType


class PaymentService:
    def __init__(
        self,
        repository: PaymentRepositoryPort,
        order_repository: OrderRepositoryPort,
        gateway: PaymentGateway,
    ):
        self._repo = repository
        self._order_repository = order_repository
        self.gateway = gateway

    async def list_payments(self, page: int = 1, size: int = 10) -> List[Payment]:
        offset = (page - 1) * size
        return await self._repo.list_payments(offset=offset, limit=size)

    async def list_pix_payments(self, page: int = 1, size: int = 10) -> List[Payment]:
        def is_pix(payment: Payment) -> bool:
            return payment.payment_type == PaymentType.PIX

        payments = await self.list_payments(page=page, size=size)
        pix_payments = list(filter(is_pix, payments))

        return pix_payments

    async def create_payment(self, payment_dto: CreatePaymentDTO) -> Payment:
        payment = Payment(
            id=uuid4(),
            order_id=payment_dto.order_id,
            amount=payment_dto.amount,
            payment_type=payment_dto.payment_type,
            payment_date=datetime.now(timezone.utc),
        )
        await self._repo.save_payment(payment)
        return payment

    async def process_payment(
        self, order_id: UUID, payment_id: UUID
    ) -> Transaction | None:
        order = await self._order_repository.get_order_by_id(order_id)
        payment = await self._repo.get_payment_by_id(payment_id)
        if order and payment is not None:
            if order.status != OrderStatus.AwaitingPayment:
                raise ValueError("Pedido em estado inválido.")

            # Pix gateway call TODO: Implement pix gateway
            # resp = self.pix_gateway.create_charge(amount=order.amount, external_id=order.id)

            order.status = OrderStatus.PaymentCompleted
            await self._order_repository.save_order(order)

            transaction = Transaction(
                id=uuid4(),
                items=order.items,
                back_urls={
                    "success": "https://127.0.0.1:8000/success",
                    "failure": "https://127.0.0.1:8000/failure",
                    "pending": "https://127.0.0.1:8000/pending",
                },
            )

            return transaction

    def generate_link(self, payment_data: Transaction) -> str:
        return self.gateway.create_payment_link(payment_data.model_dump())
