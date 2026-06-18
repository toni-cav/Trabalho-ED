from src.data_structures.ordem import Ordem
from src.data_structures.motor_match import Motor_Match
from src.data_structures.node import Node

print("Teste Motor de Match")

motor = Motor_Match()

ordem1 = Ordem(1, "C", 100.0, 50)
ordem2 = Ordem(2, "V", 95.0, 30)
ordem3 = Ordem(3, "V", 110.0, 20)
ordem4 = Ordem(4, "C", 120.0, 10)

print("\nProcessando ordem 1")
motor.processar_ordem(ordem1)
motor.imprimir_livro()

print("\nProcessando ordem 2")
motor.processar_ordem(ordem2)
motor.imprimir_livro()

print("\nProcessando ordem 3")
motor.processar_ordem(ordem3)
motor.imprimir_livro()

print("\nProcessando ordem 4")
motor.processar_ordem(ordem4)
motor.imprimir_livro()

motor.imprimir_transacoes()
