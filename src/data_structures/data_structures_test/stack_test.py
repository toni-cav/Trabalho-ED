from src.data_structures.stack import Stack


pilha = Stack()

# 1. Testando o esta_vazia inicial
print("\nPilha inicia vazia?", pilha.esta_vazia()) # Tem que ser True

# 2. Inserindo IDs de ordens no sistema (push)
print("\nInserindo ordens 101, 102 e 103...")
pilha.push(101) 
pilha.push(102) 
pilha.push(103) 

# 3. Testando o peek
print("Quem esta no topo?", pilha.peek()) # Tem que ser 103

# 4. Testando o pop (LIFO: tem que sair do ultimo pro primeiro)
print("\nDesfazendo operacoes (pop):")
print("Saiu:", pilha.pop()) # Tem que ser 103
print("Saiu:", pilha.pop()) # Tem que ser 102

# 5. Sobrou alguem?
print("\nNovo topo apos as remocoes:", pilha.peek()) # Tem que ser 101
print("Pilha esta vazia?", pilha.esta_vazia()) # Tem que ser False