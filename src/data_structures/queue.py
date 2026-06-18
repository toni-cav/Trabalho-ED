from src.data_structures.node import Node
from src.data_structures.ordem import Ordem


class Queue:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def empilhar(self, ordem: Ordem):
        novo_no = Node(ordem)

        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.next = novo_no
            novo_no.prev = self.fim
            self.fim = novo_no

        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            print("Fila vazia")
            return None

        no_removido = self.inicio
        ordem_removida = no_removido.data

        self.inicio = self.inicio.next

        if self.inicio is None:
            self.fim = None
        else:
            self.inicio.prev = None

        no_removido.next = None
        no_removido.prev = None

        self.tamanho -= 1

        return ordem_removida

    def espiar(self):
        if self.esta_vazia():
            return None

        return self.inicio.data

    def imprimir(self):
        atual = self.inicio
        saida = ""

        while atual:
            ordem = atual.data
            saida += f'{ordem.tipo} por {ordem.preco} --> '
            atual = atual.next

        return saida