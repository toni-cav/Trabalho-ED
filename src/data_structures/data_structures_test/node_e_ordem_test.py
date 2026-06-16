from ordem import Ordem
from node import Node

o1 = Ordem(id_ordem=1, tipo='c', preco=15.50, quantidade=100)
o2 = Ordem(id_ordem=2, tipo='v', preco=16.00, quantidade=50)

n1 = Node(o1)
n2 = Node(o2)

n1.next = n2
n2.prev = n1

print("Testando valores puros:")
print(n1.data.id, n1.data.tipo, n1.data.preco)

print("\nTestando os ponteiros:")
print("n1.next aponta pro id:", n1.next.data.id) # tem que ser 2
print("n2.prev aponta pro id:", n2.prev.data.id) # tem que ser 1

print("\nTestando as pontas soltas (tem que ser True):")
print(n1.prev == None) 
print(n2.next == None)