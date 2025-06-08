import pytest
from uuid import UUID
from datetime import datetime
from adapters.outbound.mock_order_repository import MockOrderRepository
from domain.entities.product import Product
from domain.entities.order import OrderStatus
from application.services.order_service import OrderService

@pytest.mark.asyncio
async def test_criar_pedido_deve_retornar_pedido_criado():
    # Preparação
    repositorio = MockOrderRepository()
    servico = OrderService(repositorio)
    
    itens = [
        
        Product(
            id="96a82c57-6480-4e3c-aef6-587c61a440fd", 
            title="Hamburgue",
            quantity=1,
            currency_id="BRL",
            unit_price=50.0
        ) 

    ]

    total = sum(p.unit_price for p in itens)

    # Ação
    pedido = await servico.create_order(items=itens, total=total)

    # Verificações
    assert pedido.id is not None
    assert isinstance(pedido.id, UUID)
    assert pedido.total == total
    assert pedido.items == itens
    assert pedido.status == OrderStatus.InProgress
    assert isinstance(pedido.order_date, datetime)

    # Verifica se o pedido foi salvo no repositório
    todos_pedidos = await repositorio.list_orders()
    assert len(todos_pedidos) == 1
    assert todos_pedidos[0].id == pedido.id