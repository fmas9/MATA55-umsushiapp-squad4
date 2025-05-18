from enum import Enum

class OrderStatus(Enum):
    InProgress = "InProgress"
    AwaitingPayment = "AwaitingPayment"
    PaymentCompleted = "PaymentCompleted"
    Completed = "Completed"