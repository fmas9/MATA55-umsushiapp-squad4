from dataclasses import dataclass
from enum import Enum
from uuid import UUID
from datetime import datetime
from typing import List
from pydantic import BaseModel
from enums.order_type import OrderStatus

class Order(BaseModel):
    id: UUID
    order_date: datetime
    items: List[str]
    total: float
    status: OrderStatus = OrderStatus.InProgress  # Use enum and default to InProgress
