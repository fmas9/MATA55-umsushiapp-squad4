from uuid import UUID

from enums.currency_type import CurrencyType
from pydantic import BaseModel


class Product(BaseModel):
    id: UUID
    title: str
    quantity: int
    currency_id: CurrencyType = CurrencyType.BRL
    unit_price: float
