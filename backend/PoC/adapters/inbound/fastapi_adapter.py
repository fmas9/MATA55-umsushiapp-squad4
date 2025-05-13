from typing import List
from fastapi import FastAPI, Depends, HTTPException, status, Query
from adapters.outbound.mock_payment_repository import MockPaymentRepository
from application.services.order_service import OrderService
from application.services.payment_service import PaymentService
from adapters.outbound.mock_order_repository import MockOrderRepository
from domain.dtos.order_create import CreateOrderDTO
from domain.dtos.payment_create import CreatePaymentDTO
from domain.entities.payment import Payment
from domain.entities.order import Order

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
    payload: CreateOrderDTO,
    service: OrderService = Depends(get_order_service)
):
    if not payload.items or payload.total <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid order payload"
        )
    return await service.create_order(items=payload.items, total=payload.total)

async def get_payment_repository() -> MockPaymentRepository:
    # In production, you could return a real implementation
    return payment_repository

# Dependency injection for service
def get_payment_service(
    repo: MockPaymentRepository = Depends(get_payment_repository),
) -> PaymentService:
    return PaymentService(repository=repo, order_repository=repository_instance)

@app.get("/payments/pix")
def list_pix_payments():
    return payment_repository.list_payments()["pix"]

# Create payments
@app.post(
        "/payments", 
        response_model=Payment,
        status_code=status.HTTP_201_CREATED
    )
async def create_payment(
    payment: CreatePaymentDTO,
    service: PaymentService = Depends(get_payment_service),
):
    if not payment.amount > 0:
         raise HTTPException(
             status_code=status.HTTP_400_BAD_REQUEST,
             detail="Invalid payment payload."
         )
    payment = await service.create_payment(payment)
    return payment

# Payments history
@app.get("/payments", response_model=List[Payment])
async def list_payments(
    service: PaymentService = Depends(get_payment_service),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    return await service.list_payments(page=page, size=size)
