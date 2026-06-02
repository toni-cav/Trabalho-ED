from src.models.node import Node

# Teste 1 com nós com o mesmo tipo de dado

lista_1 = Node([1, 2, 5, 4, 0.8])
lista_2 = Node([1, 2, 5, 4, 0.8, 8 , 3, 1], lista_1)
lista_3 = Node([1, 2, 5, 4, 0.8, 8 , 3, 1, 8, 9, 0])

lista_3.prev = lista_2
lista_2.next = lista_3

lista_1.next = lista_2 

print(lista_1.data, lista_1.next.data, lista_3.prev.data)

# Teste 2 com nós vazios 

lista_100 = Node("Nenhum dado encontrado")
print(lista_100.next == None, lista_100.prev == None)

# Teste 3 mutabilidade dos nós com dados diferentes

lista_1.data = 0
print(lista_1.data, lista_1.next.data, lista_3.prev.data)

