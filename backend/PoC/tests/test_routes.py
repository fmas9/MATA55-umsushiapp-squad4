import json
from http import HTTPStatus

import requests

base = "http://localhost"
port = "8000"

url = f"{base}:{port}"


def tester(message: str):
    def decorator(f):
        def wrapper(*args):
            print(message)
            result = f(*args)
            input("Aperte <Enter>\n")

            return result

        return wrapper

    return decorator


@tester(
    "Este programa testa automaticamente as rotas '/orders' e '/payments', enviando requisições POST e GET, para criar e ler os recursos do sistema.\n"
)
def init():
    pass


@tester(
    f"Enviando requisição GET na url: {url}/orders/, para listar os pedidos salvos.\n"
)
def test_list_orders():
    res = requests.get(f"{url}/orders")

    assert res.status_code == HTTPStatus.OK
    assert type(res.json()) is list
    print(
        f"status code: {res.status_code}\nconteudo: {res.json()}\n\nlist_orders OK.\n",
    )


@tester(f"Enviando requisição POST na url: {url}/orders/, para criar um novo pedido.\n")
def test_create_order():
    new_order = {"items": ["Acarajé", "Coca-Cola"], "total": 15.50}

    res = requests.post(f"{url}/orders", json.dumps(new_order))

    assert res.status_code == HTTPStatus.CREATED
    assert type(res.json()) is dict

    order_id = res.json()["id"]

    print(
        f"status code: {res.status_code}\nid do novo pedido: {order_id}\n\ncreate_order OK.\n"
    )

    return order_id


@tester(
    f"Enviando requisição POST na url: {url}/payments/, para criar um novo pagamento com o id obtido anteriomente.\n"
)
def test_create_payment(order_id):
    new_payment = {"order_id": order_id, "amount": 15.50, "payment_type": "pix"}
    res = requests.post(f"{url}/payments", json.dumps(new_payment))

    assert res.status_code == HTTPStatus.CREATED
    assert type(res.json()) is dict

    payment_id = res.json()["id"]

    print(
        f"status code: {res.status_code}\nid do novo pagamento: {payment_id}\n\ncreate_payment OK.\n"
    )


@tester(
    f"Enviando requisição GET na url: {url}/payments/, para listar os pagamentos salvos.\n"
)
def test_list_payments():
    res = requests.get(f"{url}/payments")

    assert res.status_code == HTTPStatus.OK
    assert type(res.json()) is list

    print(
        f"status code: {res.status_code}\nconteudo: {res.json()}\n\nlist_payment OK.\n"
    )


@tester(
    f"Enviando requisição GET na url: {url}/payments/pix, para listar os pagamentos pix salvos.\n"
)
def test_list_pix_payments():
    res = requests.get(f"{url}/payments/pix")

    assert res.status_code == HTTPStatus.OK
    assert type(res.json()) is list

    for payment in res.json():
        assert payment["payment_type"] == "pix"

    print(
        f"status code: {res.status_code}\nconteudo: {res.json()}\n\nlist_pix_payment OK.\n"
    )


init()
test_list_orders()
order_id = test_create_order()
test_create_payment(order_id)
test_list_payments()
test_list_pix_payments()
