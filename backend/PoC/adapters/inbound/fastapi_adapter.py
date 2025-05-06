from adapters.outbound.mock_payment_repository import MockPaymentRepository
from domain.dtos.payment_create import PaymentCreateDTO
from fastapi import FastAPI, Depends, HTTPException, status, Query
from typing import List
from uuid import UUID
from domain.models import Order
from application.services import OrderService
from adapters.outbound.mock_repository import MockOrderRepository
from domain.dtos.order_create import CreateOrderRequest

app = FastAPI()

# Repository instances, to use cached life cycle MockOrder
repository_instance = MockOrderRepository()
payment_repository = MockPaymentRepository() # TODO: Create PaymentService and change instance uses 

# Dependency injection for repository (can be overridden in tests)
# Injeção de dependencia para repositório de pedido (Pode ser alterado em testes futuros)
async def get_order_repository() -> MockOrderRepository:
    # In production, you could return a real implementation
    return repository_instance

# Dependency injection for service
def get_order_service(
    repo: MockOrderRepository = Depends(get_order_repository)
) -> OrderService:
    return OrderService(repository=repo)

# Retornará a lista de pedidos da sessão
@app.get("/orders", response_model=List[Order])
async def list_orders(
    service: OrderService = Depends(get_order_service),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    return await service.list_orders(page=page, size=size)

@app.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(
    payload: CreateOrderRequest,
    service: OrderService = Depends(get_order_service)
):
    if not payload.items or payload.total <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid order payload"
        )
    return await service.create_order(items=payload.items, total=payload.total)

@app.post("/payments")
def create_payment(payment: PaymentCreateDTO):
    return payment_repository.create_payment(payment)

@app.get("/payments")
def list_payments():
    return payment_repository.list_payments()

@app.get("/payments/pix")
def list_payments():
    return payment_repository.list_payments()