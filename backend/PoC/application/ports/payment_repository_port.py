from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.entities.payment import Payment

class PaymentRepositoryPort(ABC):
    @abstractmethod
    async def list_payments(self, offset: int = 0, limit: int = 10) -> List[Payment]:
        pass

    @abstractmethod
    async def save_payment(self, payment: Payment) -> None:
        pass

    @abstractmethod
    async def get_payment_by_id(self, payment_id: UUID)  -> Payment | None:
        pass
