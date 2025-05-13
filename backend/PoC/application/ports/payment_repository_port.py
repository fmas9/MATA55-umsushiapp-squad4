from abc import ABC, abstractmethod
from typing import List
from domain.entities.payment import Payment

class PaymentRepositoryPort(ABC):
    @abstractmethod
    async def list_payments(self, offset: int = 0, limit: int = 10) -> List[Payment]:
        pass

    @abstractmethod
    async def process_payment(self, payment_id: str, payment: Payment) -> None:
        pass

    @abstractmethod
    async def save_payment_history(self, payment: Payment) -> None:
        pass
