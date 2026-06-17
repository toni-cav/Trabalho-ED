from src.data_structures.ordem import Ordem
from src.data_structures.motor_match import Motor_Match

print("=== TESTE FILA DE ENTRADA ===")

motor = Motor_Match()

ordem1 = Ordem(1, "C", 100.0, 10)
ordem2 = Ordem(2, "V", 110.0, 5)
ordem3 = Ordem(3, "C", 105.0, 8)
ordem4 = Ordem(4, "V", 115.0, 3)

motor.inserir_ordem(ordem1)
motor.inserir_ordem(ordem2)
motor.inserir_ordem(ordem3)
motor.inserir_ordem(ordem4)

print("\nTamanho da fila antes de processar (tem que ser 4):", motor.fila_entrada.tamanho)

motor.processar_fila()

print("\nFila vazia depois de processar (tem que ser True):", motor.fila_entrada.esta_vazia())

motor.imprimir_livro()
# Compras esperado: 105 --> 100 (maior preço primeiro)
# Vendas esperado: 110 --> 115 (menor preço primeiro)


print("\n=== TESTE SISTEMA DE UNDO (desfazer_ultima_acao) ===")

print("\nDesfazendo a última ordem inserida no livro (ordem 4, venda a 115):")
motor.desfazer_ultima_acao()

motor.imprimir_livro()
# A venda a 115 deve ter desaparecido, restando só a venda a 110

print("\nDesfazendo novamente (ordem 3, compra a 105):")
motor.desfazer_ultima_acao()

motor.imprimir_livro()
# A compra a 105 deve ter desaparecido, restando só a compra a 100


print("\n=== TESTE UNDO COM ORDEM JÁ CASADA ===")

motor2 = Motor_Match()

ordem5 = Ordem(5, "V", 50.0, 5)
ordem6 = Ordem(6, "C", 50.0, 5)  # casa totalmente com a ordem 5

motor2.inserir_ordem(ordem5)
motor2.inserir_ordem(ordem6)
motor2.processar_fila()

motor2.imprimir_livro()
# Livro deve estar vazio, as duas ordens se casaram completamente

print("\nTentando desfazer a ordem 5, que já foi casada:")
resultado = motor2.desfazer_ultima_acao()
print("Resultado do undo (tem que ser None):", resultado)


print("\n=== TESTE UNDO COM PILHA VAZIA ===")

motor3 = Motor_Match()
print("\nTentando desfazer sem nenhuma ação no histórico:")
resultado_vazio = motor3.desfazer_ultima_acao()
print("Resultado do undo (tem que ser None):", resultado_vazio)