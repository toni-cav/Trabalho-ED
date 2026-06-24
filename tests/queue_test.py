from src.data_structures.ordem import Ordem
from src.data_structures.queue import Queue

print("Teste Queue")

fila = Queue()

ordem1 = Ordem(1, "C", 100.0, 10)
ordem2 = Ordem(2, "V", 90.0, 5)
ordem3 = Ordem(3, "C", 110.0, 20)

fila.empilhar(ordem1)
fila.empilhar(ordem2)
fila.empilhar(ordem3)

print("Fila inicial:")
print(fila.imprimir())

print("\nPrimeira ordem da fila sem remover:")
print(fila.espiar())

print("\nRemovendo da fila:")
print(fila.desempilhar())
print(fila.desempilhar())

print("\nFila depois das remoções:")
print(fila.imprimir())
