# backend/PoC/tests/unit/test_dtos/test_create_order_dto.py

import pytest
from pydantic import ValidationError

# AJUSTE ESTE CAMINHO se o seu arquivo CreateOrderDTO.py estiver em outro lugar
from backend.PoC.domain.dtos.order_create import CreateOrderDTO, ItemDTO


def test_create_order_dto_with_valid_data():
    """
    Testa a criação de CreateOrderDTO com dados válidos.
    Deve ser bem-sucedido e os atributos devem ser definidos corretamente.
    """
    valid_data = {
        "items": [
            {"product_id": "pizza-mussarela", "quantity": 2, "price": 45.00},
            {"product_id": "coca-cola", "quantity": 1, "price": 8.00}
        ],
        "total": 98.00
    }

    # CORREÇÃO AQUI: Adicionado 'CreateOrderDTO' antes de (**valid_data)
    order_dto = CreateOrderDTO(**valid_data)

    assert order_dto.total == 98.00
    assert len(order_dto.items) == 2
    assert order_dto.items[0].product_id == "pizza-mussarela"
    assert order_dto.items[1].quantity == 1
    assert isinstance(order_dto.items[0], ItemDTO)


def test_create_order_dto_with_empty_items_list_invalid():
    """
    Testa a criação de CreateOrderDTO com uma lista de 'items' vazia.
    Deve levantar ValidationError porque 'items' tem 'min_items=1'.
    """
    invalid_data = {
        "items": [],
        "total": 10.00
    }
    with pytest.raises(ValidationError) as excinfo:
        # CORREÇÃO AQUI: Adicionado 'CreateOrderDTO' antes de (**invalid_data)
        CreateOrderDTO(**invalid_data)
    assert "ensure this value has at least 1 item" in str(excinfo.value)
    assert "items" in str(excinfo.value)

def test_create_order_dto_with_negative_total_invalid():
    """
    Testa a criação de CreateOrderDTO com um 'total' negativo.
    Deve levantar ValidationError porque 'total' tem 'gt=0'.
    """
    invalid_data = {
        "items": [
            {"product_id": "prod-abc", "quantity": 1, "price": 10.0}
        ],
        "total": -1.00
    }
    with pytest.raises(ValidationError) as excinfo:
        # CORREÇÃO AQUI: Adicionado 'CreateOrderDTO' antes de (**invalid_data)
        CreateOrderDTO(**invalid_data)
    assert "ensure this value is greater than 0" in str(excinfo.value)
    assert "total" in str(excinfo.value)

def test_create_order_dto_with_item_zero_quantity_invalid():
    """
    Testa a criação de CreateOrderDTO com um item que tem 'quantity' zero.
    Deve levantar ValidationError porque 'quantity' tem 'gt=0'.
    """
    invalid_data = {
        "items": [
            {"product_id": "prod-abc", "quantity": 0, "price": 10.0}
        ],
        "total": 0.00
    }
    with pytest.raises(ValidationError) as excinfo:
        # CORREÇÃO AQUI: Adicionado 'CreateOrderDTO' antes de (**invalid_data)
        CreateOrderDTO(**invalid_data)
    assert "ensure this value is greater than 0" in str(excinfo.value)
    assert "items.0.quantity" in str(excinfo.value)

def test_create_order_dto_missing_required_field():
    """
    Testa a criação de CreateOrderDTO faltando um campo obrigatório ('items').
    Deve levantar ValidationError.
    """
    invalid_data = {
        "total": 25.00
    }
    with pytest.raises(ValidationError) as excinfo:
        # CORREÇÃO AQUI: Adicionado 'CreateOrderDTO' antes de (**invalid_data)
        CreateOrderDTO(**invalid_data)
    assert "field required" in str(excinfo.value)
    assert "items" in str(excinfo.value)