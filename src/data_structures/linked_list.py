from node import Node
from datetime import datetime

class Linked_List_Compra: # Melhor comprador no início

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
                    atual.anterior.proximo = no
                
                atual.anterior = no
                self.tamanho += 1
                return # O RETURN QUEBRA O LOOP INFINITO!

            # Caso o preço seja o menor de todos (vai ser inserido no final da lista)
            if atual.proximo is None:
                atual.proximo = no
                no.anterior = atual
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
    print(lista_compradores.imprimir())
    lista_compradores.adicionar_no(acao2)
    print(lista_compradores.imprimir())