import time

class Ordem:
    # objeto que representa uma "ordem" no simulador.

    def __init__(self, id_ordem: int, tipo: str, preco: float, quantidade: int):
        self.id = id_ordem
        self.tipo = tipo.upper()
        self.preco = preco
        self.quantidade = quantidade
        self.timestamp = time.time()

        if self.tipo not in ("C", "V"):
            raise ValueError("Tipo da ordem deve ser 'C' para compra ou 'V' para venda.")
        
        if self.preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        
        if self.quantidade <= 0:
            raise ValueError("A quatidade deve ser maior que zero.")
        

    def __repr__(self):
        # formata a exibição da ordem no terminal para facilitar testes e debug
        return (
            f"Ordem("
            f"id={self.id}, "
            f"tipo='{self.tipo}', "
            f"preco={self.preco:.2f}, "
            f"quantidade={self.quantidade}"
            f")"
        )