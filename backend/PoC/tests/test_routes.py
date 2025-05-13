import json

import requests

base = "http://localhost"
port = "8000"

url = f"{base}:{port}"

print(
    "Este programa testa automaticamente as rotas '/orders' e '/payments', enviando requisições POST e GET, para criar e ler os recursos do sistema.\n"
)

input("Aperte <Enter>\n")

# GET na rota /orders
print(
    f"Enviando requisição GET na url: {url}/orders/, para listar os pedidos salvos.\n"
)
res = requests.get(f"{url}/orders")

if res.status_code == 200 and type(res.json()) is list:
    print(f"status code: {res.status_code}\n", f"conteudo: {res.json()}\n")

input("Aperte <Enter>\n")

# POST na rota /orders
new_order = {"items": ["Acarajé", "Coca-Cola"], "total": 15.50}

print(f"Enviando requisição POST na url: {url}/orders/, para criar um novo pedido.\n")
res = requests.post(f"{url}/orders", json.dumps(new_order))

if res.status_code == 201:
    id = res.json()["id"]
    print(f"status code: {res.status_code}\n", f"id do novo pedido: {id}\n")

input("Aperte <Enter>\n")

# POST na rota /payments
new_payment = {"order_id": id, "amount": new_order["total"], "payment_type": "pix"}

print(
    f"Enviando requisição POST na url: {url}/payments/, para criar um novo pagamento com o id obtido anteriomente.\n"
)
res = requests.post(f"{url}/payments", json.dumps(new_payment))

if res.status_code == 201:
    id = res.json()["id"]
    print(f"status code: {res.status_code}\n", f"id do novo pagamento: {id}\n")

input("Aperte <Enter>\n")

# GET na rota /payments
print(
    f"Enviando requisição GET na url: {url}/payments/, para listar os pagamentos salvos.\n"
)
res = requests.get(f"{url}/payments")

if res.status_code == 200 and type(res.json()) is list:
    print(f"status code: {res.status_code}\n", f"conteudo: {res.json()}\n")

input("Aperte <Enter>\n")
