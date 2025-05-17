from datetime import datetime, timezone
from typing import List
from uuid import UUID, uuid4

from application.ports.order_repository_port import OrderRepositoryPort
from application.ports.payment_repository_port import PaymentRepositoryPort
from domain.dtos.payment_create import CreatePaymentDTO
from domain.entities.order import OrderStatus
from domain.entities.payment import Payment


class PaymentService:
    def __init__(
        self, repository: PaymentRepositoryPort, order_repository: OrderRepositoryPort
    ):
        self._repo = repository
        self._order_repository = order_repository

    async def list_payments(self, page: int = 1, size: int = 10) -> List[Payment]:
        offset = (page - 1) * size
        return await self._repo.list_payments(offset=offset, limit=size)

    async def create_payment(self, payment_dto: CreatePaymentDTO) -> Payment:
        payment = Payment(
            id=uuid4(),
            order_id=payment_dto.order_id,
            amount=payment_dto.amount,
            payment_type=payment_dto.payment_type,
            payment_date=datetime.now(timezone.utc),
        )
        await self._repo.save_payment_history(payment)
        return payment

    async def process_payment(
        self, order_id: str
    ) -> dict[str, UUID | OrderStatus] | None:
        order = await self._order_repository.get_order_by_id(order_id)
        # print("D\Exceção aqui {}".format(order))

        if order is not None:
            if order.status != OrderStatus.AwaitingPayment:
                raise ValueError("Pedido em estado inválido.")
            # Pix gateway call TODO: Implement pix gateway
            # resp = self.pix_gateway.create_charge(amount=order.amount, external_id=order.id)

            order.status = OrderStatus.PaymentCompleted
            await self._order_repository.save_order(order)
            return {
                "order_id": order.id,
                "new_status": order.status,
            }  # {"order_id": order.id, "new_status": order.status, "pix_key": resp["pix_key"]}
