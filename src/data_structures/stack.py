from src.data_structures.node import Node

class Stack:
    def __init__(self):
        self.topo = None
    
    def esta_vazia(self):
        if self.topo == None: return True
        else: return False

    def push(self, data):
        no = Node(data=data)

        no.next = self.topo

        self.topo = no

    def pop(self):
        if self.esta_vazia(): return None
        
        no_removido = self.topo.data

        self.topo = self.topo.next

        return no_removido
    
    def peek(self):
        if self.esta_vazia(): return None

        return self.topo.data
