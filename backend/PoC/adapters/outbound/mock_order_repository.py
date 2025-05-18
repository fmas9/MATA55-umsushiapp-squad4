from typing import List
from uuid import UUID

from application.ports.order_repository_port import OrderRepositoryPort
from domain.entities.order import Order, OrderStatus


class MockOrderRepository(OrderRepositoryPort):
    def __init__(self):
        self._orders: List[Order] = []

    async def list_orders(self, offset: int = 0, limit: int = 10) -> List[Order]:
        return self._orders[offset : offset + limit]

    async def get_order_by_id(self, order_id: UUID) -> Order | None:
        for order in self._orders:
            if order.id == order_id:
                return order
        return None

    # Implementação de atualiação ou append caso adicionado novo dado,
    # Para evitar duplicatas
    async def save_order(self, order: Order) -> None:
        for idx, existing_order in enumerate(self._orders):
            if existing_order.id == order.id:
                self._orders[idx] = order  # Atualiza
                return
        self._orders.append(order) 

    async def checkout_order(self, order_id: str) -> Order | None:
        order = await self.get_order_by_id(order_id)
        if order and order.status == OrderStatus.InProgress:
            order.status = OrderStatus.AwaitingPayment
            print(f"Pedido {order_id} enviado para checkout (Aguardando pagamento).")
            return order
        return None
