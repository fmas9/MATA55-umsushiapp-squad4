from domain.entities.payment import Payment
from domain.dtos.payment_create import PaymentCreateDTO
from uuid import uuid4
from datetime import datetime

class MockPaymentRepository:
    def __init__(self):
        self.payments = []

    def create_payment(self, payment_dto: PaymentCreateDTO) -> Payment:
        payment = Payment(
            id=uuid4(),
            order_id=payment_dto.order_id,
            amount=payment_dto.amount,
            payment_type=payment_dto.payment_type,
            payment_date=datetime.now()
        )
        self.payments.append(payment)
        return payment

    def list_payments(self):
        return self.payments
