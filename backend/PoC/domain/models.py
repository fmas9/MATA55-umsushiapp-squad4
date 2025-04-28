from dataclasses import dataclass
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from typing import List, Any

class OrderStatus(Enum):
    InProgress = "InProgress"
    AwaitingPayment = "AwaitingPayment"
    Completed = "Completed"

@dataclass
class Order:
    id: UUID
    order_date: datetime
    items: List[Any]
    total_value: float
    status: OrderStatus
