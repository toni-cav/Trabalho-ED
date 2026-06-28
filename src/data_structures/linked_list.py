from src.data_structures.node import Node
from src.data_structures.linked_list_base import LinkedListBase
from src.models.transacoes import Transacao


class Linked_List_Compra(LinkedListBase):

    def adicionar_no(self, no: Node):
        if no.data.tipo != 'C':
            print('Erro, tipo da ordem inválido para lista de compras')
            return

        if self.esta_vazia():
            self._inserir_vazio(no)
            return

        atual = self.inicio

        while atual:
            # Compra: maior preço deve vir antes
            if atual.data.preco < no.data.preco:
                no.next = atual
                no.prev = atual.prev

                if atual.prev is None:
                    self.inicio = no
                else:
                    atual.prev.next = no

                atual.prev = no
                self.tamanho += 1
                return

            if atual.next is None:
                self._inserir_no_fim(no)
                return

            atual = atual.next

    def imprimir(self):
        if self.esta_vazia():
            return "Nenhuma ordem de compra no livro."

        atual = self.inicio
        resultado = ""

        while atual:
            if resultado:
                resultado += " --> "
            resultado += f'{atual.data.tipo} por {atual.data.preco}'
            atual = atual.next

        return resultado


class Linked_List_Venda(LinkedListBase):

    def adicionar_no(self, no: Node):
        if no.data.tipo != 'V':
            print('Erro, tipo da ordem inválido para lista de vendas')
            return

        if self.esta_vazia():
            self._inserir_vazio(no)
            return

        atual = self.inicio

        while atual:
            # Venda: menor preço deve vir antes
            if atual.data.preco > no.data.preco:
                no.next = atual
                no.prev = atual.prev

                if atual.prev is None:
                    self.inicio = no
                else:
                    atual.prev.next = no

                atual.prev = no
                self.tamanho += 1
                return

            if atual.next is None:
                self._inserir_no_fim(no)
                return

            atual = atual.next

    def imprimir(self):
        if self.esta_vazia():
            return "Nenhuma ordem de venda no livro."

        atual = self.inicio
        resultado = ""

        while atual:
            if resultado:
                resultado += " --> "
            resultado += f'{atual.data.tipo} por {atual.data.preco}'
            atual = atual.next

        return resultado


class Linked_List_Transacoes(LinkedListBase):

    def adicionar_no(self, no: Node):
        if not isinstance(no.data, Transacao):
            print('Erro, tipo de dado inválido para lista de transações')
            return

        if self.esta_vazia():
            self._inserir_vazio(no)
            return

        self._inserir_no_fim(no)

    def imprimir(self):
        if self.esta_vazia():
            return "Nenhuma transação realizada."

        atual = self.inicio
        saida = ""

        while atual:
            saida += f'{atual.data}\n'
            atual = atual.next

        return saida
