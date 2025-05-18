import traceback
from typing import List
from uuid import UUID

from adapters.outbound.mock_order_repository import MockOrderRepository
from adapters.outbound.mock_payment_repository import MockPaymentRepository
from application.services.order_service import OrderService
from application.services.payment_service import PaymentService
from domain.dtos.order_create import CreateOrderDTO
from domain.dtos.payment_create import CreatePaymentDTO
from domain.entities.order import Order, OrderStatus
from domain.entities.payment import Payment
from domain.entities.transaction import Transaction
from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.responses import JSONResponse

app = FastAPI()

# Repository instances, to use cached life cycle MockOrder
repository_instance = MockOrderRepository()
payment_repository = MockPaymentRepository()


# Dependency injection for order repository (can be overridden in tests)
# Injeção de dependencia para repositório de pedido (Pode ser alterado em testes futuros)
async def get_order_repository() -> MockOrderRepository:
    return repository_instance


async def get_payment_repository() -> MockPaymentRepository:
    return payment_repository


# Dependency injection for payment service
def get_payment_service(
    repo: MockPaymentRepository = Depends(get_payment_repository),
) -> PaymentService:
    return PaymentService(repository=repo, order_repository=repository_instance)


# Dependency injection for order service
def get_order_service(
    repo: MockOrderRepository = Depends(get_order_repository),
) -> OrderService:
    return OrderService(repository=repo)


# Retornará a lista de pedidos da sessão
@app.get("/orders", response_model=List[Order])
async def list_orders(
    service: OrderService = Depends(get_order_service),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
):
    return await service.list_orders(page=page, size=size)


@app.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(
    payload: CreateOrderDTO, service: OrderService = Depends(get_order_service)
):
    if not payload.items or payload.total <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid order payload"
        )
    return await service.create_order(items=payload.items, total=payload.total)


@app.post("/orders/{order_id}/checkout", response_model=Order)
async def checkout_order(
    order_id: UUID,
    service: OrderService = Depends(get_order_service),
):
    order = await service.get_order_by_id(order_id)
    if not order:
        print(f"Pedido {order_id} não encontrado.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pedido não encontrado"
        )
    if order.status != OrderStatus.InProgress:
        print(
            f"Pedido {order_id} não pode ser enviado para checkout. Status atual: {order.status.value}"
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pedido não pode ser enviado para checkout",
        )
    # TODO: Implementar uma utilização real do checkout que valide com o payments
    checked_out_order = await service.checkout_order(order_id)
    if not checked_out_order:
        print(f"Falha ao enviar o pedido {order_id} para checkout.")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Falha no checkout"
        )
    print(f"Pedido {order_id} enviado para checkout com sucesso.")
    return checked_out_order


@app.get("/payments/pix", response_model=List[Payment])
async def list_pix_payments(
    service: PaymentService = Depends(get_payment_service),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
):
    return await service.list_pix_payments(page=page, size=size)


# Create payments
@app.post("/payments", response_model=Transaction, status_code=status.HTTP_201_CREATED)
async def create_payment(
    payment_dto: CreatePaymentDTO,
    service: PaymentService = Depends(get_payment_service),
):
    if not payment_dto.amount > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid payment payload."
        )
    payment = await service.create_payment(payment_dto)
    # return payment
    validated_payment = await service.process_payment(payment.order_id, payment.id)
    return validated_payment


# Payments history
@app.get("/payments", response_model=List[Payment])
async def list_payments(
    service: PaymentService = Depends(get_payment_service),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
):
    return await service.list_payments(page=page, size=size)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    print("Erro inesperado:", exc)
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno do servidor."},
    )
