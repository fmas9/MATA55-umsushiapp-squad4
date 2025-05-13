from pydantic import BaseModel
from enums.payment_type import PaymentType
from uuid import UUID

class CreatePaymentDTO(BaseModel):
    order_id: UUID
    amount: float
    payment_type: PaymentType
