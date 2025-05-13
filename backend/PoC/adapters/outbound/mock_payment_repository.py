from application.ports.payment_repository_port import PaymentRepositoryPort
from domain.dtos.payment_create import CreatePaymentDTO
from domain.entities.payment import Payment
from uuid import uuid4
from datetime import datetime

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
            payment_date=datetime.now()
        )
        self.payment[payment.payment_type].append(payment)
        return payment
    
    async def create_payment(self, payment_dto: CreatePaymentDTO) -> Payment:
        _payment = Payment(
            id=uuid4(),
            order_id=payment_dto.order_id,
            amount=payment_dto.amount,
            payment_type=payment_dto.payment_type,
            payment_date=datetime.now()
        )
        self._payments.append(_payment)
        return _payment

    async def list_payments(self, offset: int = 0, limit: int = 10):
        return self._payments[offset:offset + limit]
    
    async def process_payment(self, payment_id: str, payment: Payment) -> None:
        self._payments.append(payment)

    async def save_payment_history(self, payment: Payment) -> None:
        self._payments.append(payment)
