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
            saida += f'{str(atual.valor['tipo'])} por {str(atual.valor['preco'])} --> '
            atual = atual.proximo
        return saida
    

    def adicionar_no(self, no: Node): # Adiciona melhor comprador no inicio
        if no.valor['tipo'] != 'C':
            print('Erro, tipo da ação inválido')
            return
            
        if self.inicio is None:
            self.inicio = no
            self.fim = no
            self.tamanho += 1
            return
            
        atual = self.inicio

        while (atual):
            if atual.valor['preco'] < no.valor['preco']:
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

    def contem_no(self, no: Node) -> bool:
        if self.tamanho == 0 or no is None:
            print('Nó inválido ou lista vazia.')
            return False
            
        atual = self.inicio
        
        while atual is not None:
            
            # Compara se o objeto atual da lista é EXATAMENTE o mesmo
            if atual == no:
                return True
                
            # 3. O Passo (ESSENCIAL para não travar o loop!)
            atual = atual.proximo
            
        # 4. Terminou de varrer a lista e não encontrou
        return False

    def excluir_no(self, no: Node):
        # Verificando se o nó que será excuido está na lista
        if self.contem_no(no):
            pass
        else:
            return print(f" Nó: '{no.valor}' não está na lista, portanto não pode ser excluído")

        # Quando o nó é o unico da lista
        if no == self.inicio and no == self.fim:
            self.inicio = None
            self.fim = None
            
        # Quando o nó é o primeiro da lista
        elif no.anterior is None:
            self.inicio = no.proximo
            self.inicio.anterior = None
            
        # Quando o nó é o último da lista
        elif no.proximo is None:
            self.fim = no.anterior
            self.fim.proximo = None
            
        # Quando o nó está no meio da lista
        else:
            no.anterior.proximo = no.proximo
            no.proximo.anterior = no.anterior

        no.proximo = None
        no.anterior = None
        no = None
        self.tamanho -= 1



if __name__ == "__main__":

    # ! Cuidado ao criar valores. Dicionário valor está tipado

    valor1 = {
        'tipo': 'C',
        'preco': 100.0,
        'quantidade': 1,
        'timestamp': datetime.now()
    }

    valor2 = {
        'tipo': 'C',
        'preco': 200.0,
        'quantidade': 3,
        'timestamp': datetime.now()
    }

    valor3 = {
        'tipo': 'C',
        'preco': 450.0,
        'quantidade': 2,
        'timestamp': datetime.now()
    }

    acao1 = Node(valor1)
    acao2 = Node(valor2)
    acao3 = Node(valor3)

    lista_compradores = Linked_List_Compra()
    lista_compradores.adicionar_no(acao1)
    lista_compradores.adicionar_no(acao2)
    lista_compradores.excluir_no(acao3)
















    # lista_compradores = Linked_List_Compra()
    # lista_compradores.adicionar_no(acao1)
    # print(lista_compradores.imprimir())
    # #lista_compradores.adicionar_no(acao2)
    # print(lista_compradores.imprimir())
    # #lista_compradores.adicionar_no(acao3)
    # print(lista_compradores.imprimir())

    # lista_compradores.excluir_no(acao2)
    # print(lista_compradores.imprimir())