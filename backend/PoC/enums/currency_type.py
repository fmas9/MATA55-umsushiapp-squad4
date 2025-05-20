from enum import Enum


class CurrencyType(str, Enum):
    BRL = "BRL"  # Real
    USD = "USD"  # Dolar Americano
    JPY = "JPY"  # Iene Japones
    GBP = "GBP"  # Libra Esterlina
    AUD = "AUD"  # Dolar Australiano
    CAD = "CAD"  # Dolar Canadense
    CHF = "CHF"  # Franco Suiço
    CNY = "CNY"  # Yuan Chines
    HKD = "HKD"  # Dolar de Hong Kong
    NZD = "NZD"  # Dolar Neozelandes
    SEK = "SEK"  # Coroa Sueca
    KRW = "KRW"  # Won Sul-coreano
    SGD = "SGD"  # Dolar de Cingapura
