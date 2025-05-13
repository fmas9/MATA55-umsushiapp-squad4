import pytest
from OrderManager import OrderManager, Order  # Ajuste se o nome do arquivo for diferente

@pytest.mark.asyncio
async def test_save_and_list_orders():
    manager = OrderManager()

    # Criar pedidos
    order1 = Order(1, "Pizza")
    order2 = Order(2, "Burger")
    order3 = Order(3, "Sushi")

    # Salvar pedidos
    await manager.save_order(order1)
    await manager.save_order(order2)
    await manager.save_order(order3)

    # Verifica se todos os pedidos estão salvos
    all_orders = await manager.list_orders()
    assert all_orders == [order1, order2, order3]

    # Verifica paginação
    paginated = await manager.list_orders(offset=1, limit=1)
    assert paginated == [order2]

    paginated = await manager.list_orders(offset=2, limit=2)
    assert paginated == [order3]
