from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from domain.entities.order import OrderStatus
from enums.payment_type import PaymentType

class Transaction(BaseModel):
    id: UUID
    order_id: UUID
    order_status: OrderStatus
    payment_id: UUID
    payment_type: PaymentType
    payment_date: datetime
    payment_total: float
