from typing import List
from domain.models import Order
from application.ports.order_repository_port import OrderRepositoryPort

class MockOrderRepository(OrderRepositoryPort):
    def __init__(self):
        self._orders: List[Order] = []

    async def list_orders(self, offset: int = 0, limit: int = 10) -> List[Order]:
        return self._orders[offset:offset + limit]

    async def save_order(self, order: Order) -> None:
        self._orders.append(order)
