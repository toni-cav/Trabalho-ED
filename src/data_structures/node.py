from datetime import datetime
from typing import TypedDict


class Valor(TypedDict):
    tipo: str
    preco: float
    quantidade: int
    timestamp: datetime


class Node():
    def __init__(self, valor: Valor):
        self.proximo = None
        self.anterior = None
        self.valor = valor

if __name__ == '__main__':
    valor = {
        'tipo': 'v',
        'preco': 10.0,
        'quantidade': 3,
        'timestamp': datetime.now()
    }
    no = Node(valor)
    print(no.valor)