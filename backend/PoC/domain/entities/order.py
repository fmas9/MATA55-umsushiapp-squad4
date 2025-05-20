from datetime import datetime
from typing import List
from uuid import UUID

from enums.order_type import OrderStatus
from domain.entities.product import Product
from pydantic import BaseModel


class Order(BaseModel):
    id: UUID
    order_date: datetime
    items: List[Product]
    total: float # Alterar
    status: OrderStatus = OrderStatus.InProgress  # Use enum and default to InProgress
