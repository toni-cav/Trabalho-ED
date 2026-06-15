import time

class Ordem:
    # objeto que representa uma "ordem" no simulador.

    def __init__(self, id_ordem: int, tipo: str, preco: float, quantidade: int):
        # ID (int): Identificador único da ordem
        self.id = id_ordem
        
        # Tipo (char): 'C' para Compra ou 'V' para Venda
        self.tipo = tipo.upper()
        
        # Preço (float): Valor unitário que o investidor aceita pagar ou receber
        self.preco = preco
        
        # Quantidade (int): Volume de ações a serem negociadas
        self.quantidade = quantidade
        
        # Timestamp (t): Momento exato da entrada da ordem no sistema
        self.timestamp = time.time()

    def __repr__(self):
        # formata a exibição da ordem no terminal para facilitar testes e debug
        return f"Ordem(ID:{self.id}, Tipo:'{self.tipo}', Preço:R${self.preco:.2f}, Qtd:{self.quantidade})"