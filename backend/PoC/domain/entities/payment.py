from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enums.payment_type import PaymentType

class Payment(BaseModel):
    id: UUID
    order_id: UUID
    amount: float
    payment_type: PaymentType
    payment_date: datetime
