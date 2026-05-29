from datetime import datetime
import time

class Node:
    def __init__(self, id: int, type: str, price: float, quantity: int, timestamp: float):
        self.id = int(id)
        self.type = str(type)
        self.price = float(price)
        self.quantity = int(quantity)
        self.timestamp = datetime.now()