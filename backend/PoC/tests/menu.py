from typing import List
from uuid import uuid4

from pydantic import BaseModel


class TestProductDTO(BaseModel):
    id: str = str(uuid4())
    title: str
    quantity: int
    unit_price: float
    currency_id: str = "BRL"


class TestOrderDTO(BaseModel):
    items: List[TestProductDTO]
    total: float


def new_order(items: List[TestProductDTO]) -> TestOrderDTO:
    total = 0.0
    for item in items:
        total += item.unit_price * item.quantity

    return TestOrderDTO(items=items, total=total)


Acaraje = TestProductDTO(title="Acarajé", quantity=1, unit_price=12.00)
Coca_Cola = TestProductDTO(title="Coca-Cola", quantity=1, unit_price=4.00)
