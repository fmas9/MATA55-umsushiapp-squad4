from typing import List

from domain.entities.product import Product
from pydantic import BaseModel


class CreateOrderDTO(BaseModel):
    items: List[Product]
    total: float
