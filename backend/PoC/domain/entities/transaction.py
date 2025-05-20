from typing import List
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from domain.entities.order import OrderStatus
from domain.entities.product import Product
from enums.payment_type import PaymentType

class Transaction(BaseModel):
    id: UUID
    #order_id: UUID
    #order_status: OrderStatus
    items: List[Product] # MercadoPago
    # payment_id: UUID
    # payment_type: PaymentType
    # payment_date: datetime
    # payment_total: float
    back_urls: List[str] # MercadoPago
    auto_return: "all" # MercadoPago
