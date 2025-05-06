from pydantic import BaseModel
from typing import List

class CreateOrderRequest(BaseModel):
    items: List[str]
    total: float
