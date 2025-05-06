from abc import ABC, abstractmethod
from typing import List
from domain.models import Order

class OrderRepositoryPort(ABC):
    @abstractmethod
    async def list_orders(self, offset: int = 0, limit: int = 10) -> List[Order]:
        pass

    @abstractmethod
    async def save_order(self, order: Order) -> None:
        pass

