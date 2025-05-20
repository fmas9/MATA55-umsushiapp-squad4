from typing import List
from uuid import UUID

from domain.entities.product import Product
from pydantic import BaseModel


class Transaction(BaseModel):
    id: UUID
    # order_id: UUID
    # order_status: OrderStatus
    items: List[Product]  # MercadoPago
    # payment_id: UUID
    # payment_type: PaymentType
    # payment_date: datetime
    # payment_total: float
    back_urls: List[str]  # MercadoPago
    auto_return: str = "all"  # MercadoPago
