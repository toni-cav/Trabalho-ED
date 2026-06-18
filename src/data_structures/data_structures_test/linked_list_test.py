from src.data_structures.linked_list import Linked_List_Compra, Linked_List_Venda
from src.data_structures.ordem import Ordem
from src.data_structures.node import Node

print("Teste Lista de Compras")

ordem1 = Ordem(
        id_ordem=1,
        tipo='C',
        preco=100.0,
        quantidade=1
    )

ordem2 = Ordem(
        id_ordem=2,
        tipo='C',
        preco=200.0,
        quantidade=1
    )

ordem3 = Ordem(
        id_ordem=3,
        tipo='C',
        preco=150.0,
        quantidade=1
    )

acao1 = Node(ordem1)
acao2 = Node(ordem2)
acao3 = Node(ordem3)

lista_compradores = Linked_List_Compra()

lista_compradores.adicionar_no(acao1)
lista_compradores.adicionar_no(acao2)
lista_compradores.adicionar_no(acao3)

print(lista_compradores.imprimir())

print("\nTeste Lista de Vendas")

ordem4 = Ordem(
        id_ordem=4,
        tipo='V',
        preco=100.0,
        quantidade=1
    )

ordem5 = Ordem(
        id_ordem=5,
        tipo='V',
        preco=80.0,
        quantidade=1
    )

ordem6 = Ordem(
        id_ordem=6,
        tipo='V',
        preco=90.0,
        quantidade=1
    )

venda1 = Node(ordem4)
venda2 = Node(ordem5)
venda3 = Node(ordem6)

lista_vendedores = Linked_List_Venda()

lista_vendedores.adicionar_no(venda1)
lista_vendedores.adicionar_no(venda2)
lista_vendedores.adicionar_no(venda3)

print(lista_vendedores.imprimir())