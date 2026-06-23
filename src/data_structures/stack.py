from src.data_structures.node import Node

class Stack:
    def __init__(self):
        # Começa vazia
        self.topo = None
        self.tamanho = 0
    
    def esta_vazia(self):
        if self.topo == None: return True
        else: return False

    def empilhar(self, data):
        # Cria o nó a ser adicionado
        no = Node(data=data)

        # O nó aponta para o antigo item no topo
        no.next = self.topo

        # O novo item no topo é o nó adicionado
        self.topo = no

        self.tamanho += 1

    def desempilhar(self):
        # Se a lista está vazia, não há como retirar o último item
        if self.esta_vazia(): return None
        
        # Guarda o nó removido para retorná-lo
        no_removido = self.topo

        # O novo item no topo será o antigo "segundo lugar"
        self.topo = self.topo.next

        no_removido.next = None

        self.tamanho -= 1

        return no_removido.data
    
    def espiar(self):
        if self.esta_vazia(): return None
        return self.topo.data
    
    def imprimir(self):
        """
        Retorna uma string com os elementos da pilha (do topo para a base)
        para fins de debug e visualização do histórico de Undo.
        """
        if self.esta_vazia():
            return "Pilha vazia."

        atual = self.topo
        saida = "Topo -> "

        while atual:
            # Assumindo que atual.data guarda o ID da ordem
            saida += f"[{atual.data}] "
            atual = atual.next
            
        return saida
