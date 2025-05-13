from typing import List
from domain.entities.order import Order, OrderStatus
from application.ports.order_repository_port import OrderRepositoryPort
from uuid import uuid4, UUID
from datetime import datetime, timezone

class OrderService:
    def __init__(self, repository: OrderRepositoryPort):
        self.repository = repository

    async def list_orders(self, page: int = 1, size: int = 10) -> List[Order]:
        offset = (page - 1) * size
        return await self.repository.list_orders(offset=offset, limit=size)

    async def create_order(self, items: List, total: float) -> Order:
        order = Order(
            id=uuid4(),
            order_date=datetime.now(timezone.utc),
            items=items,
            total=total,  # Corrija aqui
            status=OrderStatus.InProgress
        )
        await self.repository.save_order(order)
        return order

    async def get_order_by_id(self, order_id: UUID):
        return await self.repository.get_order_by_id(order_id)

    async def checkout_order(self, order_id: UUID):
        return await self.repository.checkout_order(order_id)
