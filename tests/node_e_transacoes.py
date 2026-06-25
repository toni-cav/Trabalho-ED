from src.models.transacoes import Transacao
from src.data_structures.node import Node

print("Teste Transação")

t1 = Transacao(id_compra=1, id_venda=2, preco=15.50, quantidade=100)
t2 = Transacao(id_compra=3, id_venda=4, preco=16.00, quantidade=50)

n1 = Node(t1)
n2 = Node(t2)

n1.next = n2
n2.prev = n1

print("Testando valores puros:")
print(
    "Compra:", n1.data.id_compra,
    "| Venda:", n1.data.id_venda,
    "| Preço:", n1.data.preco,
    "| Quantidade:", n1.data.quantidade
)

print("\nTestando os ponteiros:")
print("n1.next aponta para a transação Compra ID:", n1.next.data.id_compra)
print("n2.prev aponta para a transação Compra ID:", n2.prev.data.id_compra)

print("\nTestando as pontas soltas (tem que ser True):")
print(n1.prev is None)
print(n2.next is None)

print("\nTestando a representação da transação:")
print(t1)
print(t2)