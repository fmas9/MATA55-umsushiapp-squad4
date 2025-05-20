from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def create_payment_link(self, payment_data: dict) -> str:
        """Gera um link de pagamento"""
        pass