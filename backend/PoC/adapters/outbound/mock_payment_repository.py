from datetime import datetime
from uuid import UUID, uuid4

from application.ports.payment_repository_port import PaymentRepositoryPort
from domain.dtos.payment_create import CreatePaymentDTO
from domain.entities.payment import Payment


class MockPaymentRepository(PaymentRepositoryPort):
    def __init__(self):
        self.payments = {"credit": [], "debit": [], "pix": []}
        self._payments = []

    async def create_payment_mock(self, payment_dto: CreatePaymentDTO) -> Payment:
        payment = Payment(
            id=uuid4(),
            order_id=payment_dto.order_id,
            amount=payment_dto.amount,
            payment_type=payment_dto.payment_type,
            payment_date=datetime.now(),
        )
        self.payments[payment.payment_type].append(payment)
        return payment

    async def create_payment(self, payment_dto: CreatePaymentDTO) -> Payment:
        _payment = Payment(
            id=uuid4(),
            order_id=payment_dto.order_id,
            amount=payment_dto.amount,
            payment_type=payment_dto.payment_type,
            payment_date=datetime.now(),
        )
        self._payments.append(_payment)
        return _payment

    async def list_payments(self, offset: int = 0, limit: int = 10):
        return self._payments[offset : offset + limit]

    # Implementação de atualiação ou append caso adicionado novo dado,
    # Para evitar duplicatas
    async def save_payment(self, payment: Payment) -> None:
        for idx, existing_payment in enumerate(self._payments):
            if existing_payment.id == payment.id:
                self._payments[idx] = payment  # Atualiza
                return
        self._payments.append(payment)

    async def get_payment_by_id(self, payment_id: UUID) -> Payment | None:
        for payment in self._payments:
            if payment.id == payment_id:
                return payment
        return None
