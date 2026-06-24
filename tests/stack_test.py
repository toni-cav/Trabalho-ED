from src.data_structures.stack import Stack

print("Teste Stack")

pilha = Stack()

print("\nPilha inicia vazia?", pilha.esta_vazia()) # Tem que ser True

print("\nInserindo ordens 101, 102 e 103...")
pilha.empilhar(101) 
pilha.empilhar(102) 
pilha.empilhar(103) 

print("Quem esta no topo?", pilha.espiar()) # Tem que ser 103

print("\nDesfazendo operacoes (pop):")
print("Saiu:", pilha.desempilhar()) # Tem que ser 103
print("Saiu:", pilha.desempilhar()) # Tem que ser 102

print("\nNovo topo apos as remocoes:", pilha.espiar()) # Tem que ser 101
print("Pilha esta vazia?", pilha.esta_vazia()) # Tem que ser False