import mercadopago
from application.ports.payment_gateway import PaymentGateway
from application.services.external_services.credentials import ACCESS_TOKEN


class MercadoLivreGateway(PaymentGateway):
    def __init__(self):
        self.sdk = mercadopago.SDK(ACCESS_TOKEN)

    def create_payment_link(self, payment_data: dict) -> str:
        # Convertendo os UUID's para string para que seja possivel serializar
        payment_data["id"] = str(payment_data["id"])
        for item in payment_data["items"]:
            item["id"] = str(item["id"])

        result = self.sdk.preference().create(payment_data)
        return result["response"]["init_point"]
