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


if __name__ == "__main__":

    print("=== TESTE LISTA DE COMPRAS ===")

    ordem1 = Ordem(
        id_ordem=1,
        tipo='C',
        preco=100.0,
        quantidade=1
    )

    ordem2 = Ordem(
        id_ordem=2,
        tipo='C',
        preco=200.0,
        quantidade=1
    )

    ordem3 = Ordem(
        id_ordem=3,
        tipo='C',
        preco=150.0,
        quantidade=1
    )

    acao1 = Node(ordem1)
    acao2 = Node(ordem2)
    acao3 = Node(ordem3)

    lista_compradores = Linked_List_Compra()

    lista_compradores.adicionar_no(acao1)
    lista_compradores.adicionar_no(acao2)
    lista_compradores.adicionar_no(acao3)

    print(lista_compradores.imprimir())

    print("\n=== TESTE LISTA DE VENDAS ===")

    ordem4 = Ordem(
        id_ordem=4,
        tipo='V',
        preco=100.0,
        quantidade=1
    )

    ordem5 = Ordem(
        id_ordem=5,
        tipo='V',
        preco=80.0,
        quantidade=1
    )

    ordem6 = Ordem(
        id_ordem=6,
        tipo='V',
        preco=90.0,
        quantidade=1
    )

    venda1 = Node(ordem4)
    venda2 = Node(ordem5)
    venda3 = Node(ordem6)

    lista_vendedores = Linked_List_Venda()

    lista_vendedores.adicionar_no(venda1)
    lista_vendedores.adicionar_no(venda2)
    lista_vendedores.adicionar_no(venda3)

    print(lista_vendedores.imprimir())