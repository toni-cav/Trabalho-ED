class Node:

    # estrutura base para encadeamento de nós

    def __init__(self, data=None):
        # no motor de negociação, este 'data' abrigará um objeto da classe Ordem
        self.data = data
        
        self.next = None
        
        self.prev = None