from dataclasses import dataclass
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from typing import List, Any
from pydantic import BaseModel

class OrderStatus(Enum):
    InProgress = "InProgress"
    AwaitingPayment = "AwaitingPayment"
    PaymentCompleted = "PaymentCompleted"
    Completed = "Completed"

class Order(BaseModel):
    id: UUID
    order_date: datetime
    items: List[str]
    total: float
    status: OrderStatus = OrderStatus.InProgress  # Use enum and default to InProgress
