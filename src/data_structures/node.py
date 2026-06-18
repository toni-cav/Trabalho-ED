class Node:

    # Estrutura base para encadeamento de nós

    def __init__(self, data=None):
        # No motor de negociação, este 'data' abrigará um objeto da classe Ordem
        self.data = data
        
        self.next = None
        
        self.prev = None
    
    def __repr__(self):
        return f"Node({self.data})"