from typing import Dict, List
from uuid import UUID

from domain.entities.product import Product
from pydantic import BaseModel


class Transaction(BaseModel):
    id: UUID
    items: List[Product]  # MercadoPago
    back_urls: Dict[str, str]  # MercadoPago
    auto_return: str = "all"  # MercadoPago
