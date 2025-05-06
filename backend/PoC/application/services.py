from typing import List
from domain.models import Order, OrderStatus
from application.ports import OrderRepositoryPort
from uuid import uuid4
from datetime import datetime, timezone

class OrderService:
    def __init__(self, repository: OrderRepositoryPort):
        self._repo = repository

    async def list_orders(self, page: int = 1, size: int = 10) -> List[Order]:
        offset = (page - 1) * size
        return await self._repo.list_orders(offset=offset, limit=size)

    async def create_order(self, items: List, total: float) -> Order:
        order = Order(
            id=uuid4(),
            order_date=datetime.now(timezone.utc),
            items=items,
            total_value=total,
            status=OrderStatus.AwaitingPayment
        )
        await self._repo.save_order(order)
        return order
