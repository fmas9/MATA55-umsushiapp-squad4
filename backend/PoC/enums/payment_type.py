from enum import Enum

class PaymentType(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"
    PIX = "pix"
