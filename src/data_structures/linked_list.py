from src.data_structures.node import Node
from src.data_structures.ordem import Ordem


class Linked_List_Compra:  # Melhor comprador no início

    # Construtor
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    # Imprimir itens da lista
    def imprimir(self):
        atual = self.inicio
        saida = ""

        while atual:
            saida += f'{str(atual.data.tipo)} por {str(atual.data.preco)} --> '
            atual = atual.next

        return saida


    def retorna_tamanho(self):
        return self.tamanho


    def adicionar_no(self, no: Node):  # Adiciona melhor comprador no início

        # O tipo está dentro da Ordem, e a Ordem está dentro do Node em data
        if no.data.tipo != 'C':
            print('Erro, tipo da ordem inválido para lista de compras')
            return

        # Caso 1: lista vazia
        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.tamanho += 1
            return

        atual = self.inicio

        while atual:

            # Compra: maior preço deve vir antes
            if atual.data.preco < no.data.preco:
                no.next = atual
                no.prev = atual.prev

                if atual.prev is None:
                    # Caso não haja nó antes de atual
                    self.inicio = no
                else:
                    atual.prev.next = no

                atual.prev = no
                self.tamanho += 1
                return

            # Caso o preço seja o menor de todos, insere no final
            if atual.next is None:
                atual.next = no
                no.prev = atual
                self.fim = no
                self.tamanho += 1
                return

            atual = atual.next

    def adicionar_no_meio(self, no: Node):
        if no.data.tipo != 'C':
            print('Erro, tipo da ordem inválido para lista de compras')
            return

        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.tamanho += 1
            return

        meio = self.tamanho // 2
        atual = self.inicio
        for i in range(meio):
            atual = atual.next

        no.next = atual.next
        no.prev = atual

        if atual.next is not None:
            atual.next.prev = no
        else:
            self.fim = no

        atual.next = no
        self.tamanho += 1

    
    def remover_inicio(self):
        if self.inicio is None:
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


class Linked_List_Venda:  # Melhor vendedor no início

    # Construtor
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    # Imprimir itens da lista
    def imprimir(self):
        atual = self.inicio
        saida = ""

        while atual:
            saida += f'{str(atual.data.tipo)} por {str(atual.data.preco)} --> '
            atual = atual.next

        return saida
    
    
    def retorna_tamanho(self):
        return self.tamanho
   
   
    def adicionar_no_meio(self, no: Node):
        if no.data.tipo != 'V':
            print('Erro, tipo da ordem inválido para lista de vendas')
            return

        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.tamanho += 1
            return

        meio = self.tamanho // 2
        atual = self.inicio
        for i in range(meio):
            atual = atual.next

        no.next = atual.next
        no.prev = atual

        if atual.next is not None:
            atual.next.prev = no
        else:
            self.fim = no

        atual.next = no
        self.tamanho += 1

    def adicionar_no(self, no: Node):  # Adiciona melhor vendedor no início

        # O tipo está dentro da Ordem, e a Ordem está dentro do Node em data
        if no.data.tipo != 'V':
            print('Erro, tipo da ordem inválido para lista de vendas')
            return

        # Caso 1: lista vazia
        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.tamanho += 1
            return

        atual = self.inicio

        while atual:

            # Venda: menor preço deve vir antes
            if atual.data.preco > no.data.preco:
                no.next = atual
                no.prev = atual.prev

                if atual.prev is None:
                    # Caso não haja nó antes de atual
                    self.inicio = no
                else:
                    atual.prev.next = no

                atual.prev = no
                self.tamanho += 1
                return

            # Caso o preço seja o maior de todos, insere no final
            if atual.next is None:
                atual.next = no
                no.prev = atual
                self.fim = no
                self.tamanho += 1
                return

            atual = atual.next

 
    def remover_inicio(self):
        if self.inicio is None:
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


