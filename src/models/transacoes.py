import time

class Transacao:
    def __init__(self, id_compra:int, id_venda:int, preco: float, quantidade: int):
        self.id_compra = id_compra
        self.id_venda = id_venda
        self.preco = preco
        self.quantidade = quantidade
        self.timestamp = time.time()
        if self.preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        
        if self.quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

    def __repr__(self):
        return (
            f"Transação("
            f"id_venda={self.id_venda}, "
            f"id_compra={self.id_compra},"
            f"preco={self.preco:.2f},"
            f"quantidade={self.quantidade},"
            f"instante={self.timestamp}"
            f")"
        )
        