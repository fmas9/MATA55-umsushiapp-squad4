from pydantic import BaseModel
from typing import List

class CreateOrderDTO(BaseModel):
    items: List[str]
    total: float
