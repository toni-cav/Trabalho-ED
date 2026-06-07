from datetime import datetime
import time

class Node:
    def __init__(self, tipo: str, preco: float, quantidade: int):
        self.id = None # Usar id ou não?????
        self.tipo = tipo # compra ou venda
        self.preco = preco
        self.quantidade = quantidade # quantas acoes foram compradas ou vendidas
        self.timestamp = datetime.now()
        self.proximo = None
        self.anterior = None