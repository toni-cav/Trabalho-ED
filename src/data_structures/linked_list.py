from src.data_structures.node import Node
from src.models.transacoes import Transacao

class Linked_List_Compra:  # Melhor comprador no início

    # Construtor
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    # Imprimir itens da lista
    def imprimir(self):
        if self.esta_vazia(): return "Nenhuma ordem de compra no livro."

        atual = self.inicio
        partes = []

        while atual:
            partes.append(f'{atual.data.tipo} por {atual.data.preco}')
            atual = atual.next

        return ' --> '.join(partes)
    
    def esta_vazia(self):
        if self.inicio is None: return True
        else: return False


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

    def remover_por_id(self, id_ordem):
        """
        Remove de qualquer ponto da lista o nó cuja Ordem tenha o id
        informado, religando os ponteiros next/prev dos vizinhos.
        Necessário para o cancelamento via pilha de undo.
        """
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

                ordem_removida = atual.data

                atual.next = None
                atual.prev = None

                self.tamanho -= 1
                return ordem_removida

            atual = atual.next

        return None  # id não encontrado no livro

    def retorna_tamanho(self):
        return self.tamanho

class Linked_List_Venda:  # Melhor vendedor no início

    # Construtor
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        if self.inicio is None: return True
        else: return False


    # Imprimir itens da lista
    def imprimir(self):
        if self.esta_vazia(): return "Nenhuma ordem de venda no livro."

        atual = self.inicio
        partes = []

        while atual:
            partes.append(f'{atual.data.tipo} por {atual.data.preco}')
            atual = atual.next

        return ' --> '.join(partes)

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

                ordem_removida = atual.data

                atual.next = None
                atual.prev = None

                self.tamanho -= 1
                return ordem_removida

            atual = atual.next

        return None  # id não encontrado no livro
    
class Linked_List_Transacoes:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        if self.inicio is None: return True
        else: return False

    def adicionar_no(self, no: Node):
        if not isinstance(no.data, Transacao): print('Erro, tipo de dado inválido para lista de transações'); return

        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.tamanho +=1
            return
        
        self.fim.next = no
        no.prev = self.fim
        self.fim = no
        self.tamanho += 1

    def imprimir(self):
        if self.esta_vazia(): return "Nenhuma transação realizada."
        atual = self.inicio
        saida = ""

        while atual:
            saida += f'{atual.data}\n'
            atual = atual.next

        return saida
    
    def retorna_tamanho(self):
        return self.tamanho
