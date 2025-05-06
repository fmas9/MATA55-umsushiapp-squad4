from domain.entities.payment import Payment
from application.ports.payment_repository_port import PaymentRepositoryPort
from application.ports.order_repository_port import OrderRepositoryPort
from domain.models import OrderStatus

class PaymentService:
    def __init__(self, repository: PaymentRepositoryPort, order_repository: OrderRepositoryPort):
        self._repo = repository
        self.order_repository = order_repository

    async def list_payments(self, page: int = 1, size: int = 10) -> List[Payment]:
        offset = (page - 1) * size
        return await self._repo.list_payments(offset=offset, limit=size)
    
    async def process_payment(self, order_id: str, payment: Payment) -> None:
        pass