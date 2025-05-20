import mercadopago
from credentials.credentials import ACCESS_TOKEN
from domain.ports.payment_gateway import PaymentGateway

class MercadoLivreGateway(PaymentGateway):
    def __init__(self):
        self.sdk = mercadopago.SDK(ACCESS_TOKEN)

    def create_payment_link(self, payment_data: dict) -> str:
        result = self.sdk.preference().create(payment_data)
        return result["response"]["init_point"]

    # payment_data = {
    #     "items": [
    #         {
    #             "id": "6",
    #             "title": "X Salada Sem Salada",
    #             "quantity": 1,
    #             "currency_id": "BRL",
    #             "unit_price": 12.0,
    #         }
    #     ],
    #     "back_urls": {
    #         "success": "https://127.0.0.1:8000/",
    #         "failure": "https://127.0.0.1:8000/",
    #         "pending": "https://127.0.0.1:8000/",
    #     },
    #     "auto_return": "all",
    # }