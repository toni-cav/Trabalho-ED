from src.data_structures.node import Node


class LinkedListBase:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def retorna_tamanho(self):
        return self.tamanho

    def _inserir_vazio(self, no: Node):
        self.inicio = no
        self.fim = no
        self.tamanho += 1

    def _inserir_no_fim(self, no: Node):
        self.fim.next = no
        no.prev = self.fim
        self.fim = no
        self.tamanho += 1

    def remover_inicio(self):
        if self.inicio is None:
            return None

        no_removido = self.inicio
        dado_removido = no_removido.data

        self.inicio = self.inicio.next

        if self.inicio is None:
            self.fim = None
        else:
            self.inicio.prev = None

        no_removido.next = None
        no_removido.prev = None

        self.tamanho -= 1

        return dado_removido

    def remover_por_id(self, id_ordem):
        atual = self.inicio

        while atual:
            if atual.data.id == id_ordem:

                if atual.prev is None:
                    self.inicio = atual.next
                else:
                    atual.prev.next = atual.next

                if atual.next is None:
                    self.fim = atual.prev
                else:
                    atual.next.prev = atual.prev

                dado_removido = atual.data

                atual.next = None
                atual.prev = None

                self.tamanho -= 1
                return dado_removido

            atual = atual.next

        return None
