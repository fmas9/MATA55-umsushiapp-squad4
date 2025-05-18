import json

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

    if res.status_code == 200 and type(res.json()) is list:
        print(f"status code: {res.status_code}\n", f"conteudo: {res.json()}\n")


@tester(f"Enviando requisição POST na url: {url}/orders/, para criar um novo pedido.\n")
def test_create_order():
    new_order = {"items": ["Acarajé", "Coca-Cola"], "total": 15.50}

    res = requests.post(f"{url}/orders", json.dumps(new_order))

    if res.status_code == 201:
        order_id = res.json()["id"]
        print(f"status code: {res.status_code}\n", f"id do novo pedido: {order_id}\n")

        return order_id


@tester(
    f"Enviando requisição POST na url: {url}/payments/, para criar um novo pagamento com o id obtido anteriomente.\n"
)
def test_create_payment(order_id):
    new_payment = {"order_id": order_id, "amount": 15.50, "payment_type": "pix"}
    res = requests.post(f"{url}/payments", json.dumps(new_payment))

    if res.status_code == 201:
        payment_id = res.json()["id"]
        print(
            f"status code: {res.status_code}\n", f"id do novo pagamento: {payment_id}\n"
        )


@tester(
    f"Enviando requisição GET na url: {url}/payments/, para listar os pagamentos salvos.\n"
)
def test_list_payments():
    res = requests.get(f"{url}/payments")

    if res.status_code == 200 and type(res.json()) is list:
        print(f"status code: {res.status_code}\n", f"conteudo: {res.json()}\n")


init()
test_list_orders()
order_id = test_create_order()
test_create_payment(order_id)
test_list_payments()
