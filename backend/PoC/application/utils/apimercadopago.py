import mercadopago
from credentials.credentials import ACCESS_TOKEN


def gen_payment_link():
    sdk = mercadopago.SDK(ACCESS_TOKEN)

    payment_data = {
        "items": [
            {
                "id": "6",
                "title": "X Salada Sem Salada",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 12.0,
            }
        ],
        "back_urls": {
            "success": "https://127.0.0.1:8000/",
            "failure": "https://127.0.0.1:8000/",
            "pending": "https://127.0.0.1:8000/",
        },
        "auto_return": "all",
    }
    result = sdk.preference().create(payment_data)

    payment = result["response"]
    link = payment["init_point"]

    return link
