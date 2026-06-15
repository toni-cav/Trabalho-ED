from node import Node
from datetime import datetime

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

        while (atual):
            saida += f'{str(atual.tipo)} por {str(atual.preco)} --> '
            atual = atual.proximo
        return saida
    
    def adicionar_no(self, no: Node): # Adiciona melhor comprador no inicio
        if no.tipo != 'Compra':
            print('Erro, tipo da ação inválido')
            return

        # Caso 1: lista vazia
        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.tamanho += 1
            return

        atual = self.inicio

        while (atual):
            if atual.preco < no.preco:
                no.proximo = atual
                no.anterior = atual.anterior
                
                if atual.anterior is None:
                    # Caso não haja nó antes de 'atual'
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
                
            atual = atual.proximo
                    
    


if __name__ == "__main__":

    # Criando primeira ação para teste
    acao1 = Node(
        tipo = 'Compra',
        preco = 100.0,
        quantidade = 1
    )

    acao2 = Node(
        tipo = 'Compra',
        preco = 200.0,
        quantidade = 1
    )

    lista_compradores = Linked_List_Compra()

    lista_compradores.adicionar_no(acao1)
    lista_compradores.adicionar_no(acao2)
    print(lista_compradores.imprimir())