from src.models.ordem import Ordem
from src.data_structures.queue import Queue

print("Teste Queue")

fila = Queue()

ordem1 = Ordem(1, "C", 100.0, 10)
ordem2 = Ordem(2, "V", 90.0, 5)
ordem3 = Ordem(3, "C", 110.0, 20)

fila.enfileirar(ordem1)
fila.enfileirar(ordem2)
fila.enfileirar(ordem3)

print("Fila inicial:")
print(fila.imprimir())

print("\nPrimeira ordem da fila sem remover:")
print(fila.espiar())

print("\nRemovendo da fila:")
print(fila.desenfileirar())
print(fila.desenfileirar())

print("\nFila depois das remoções:")
print(fila.imprimir())
