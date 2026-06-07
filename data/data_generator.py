import csv
import random
from datetime import datetime, timedelta

def generate_orders_csv(filename, num_orders):
    # 'C' para COMPRA e 'V' para VENDA
    order_types = ['C', 'V'] 
    
    # Tempo de início da simulação
    current_time = datetime.now()
    
    # Abre arquivo em modo de escrita ('w')
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Escreve o cabeçalho das colunas
        writer.writerow(['ID', 'Type', 'Price', 'Quantity', 'Timestamp'])
        
        # Loop para gerar cada linha de ordem
        for i in range(1, num_orders + 1):
            order_id = i
            order_type = random.choice(order_types)
            
            # Preço --> Distribuição uniforme entre 10.00 e 100.00
            price = round(random.uniform(10.0, 100.0), 2)
            
            # Quantidade --> Lotes de ações (múltiplos de 10, de 10 a 1000)
            quantity = random.randint(1, 100) * 10
            
            # Timestamp --> Adiciona de 1 a 5 segundos de intervalo entre as ordens
            current_time += timedelta(seconds=random.randint(1, 5))
            timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
            
            # Grava a linha no arquivo CSV
            writer.writerow([order_id, order_type, price, quantity, timestamp])

# Bloco de execução principal
if __name__ == "__main__":
    # Gera o arquivo de teste com 50 ordens
    generate_orders_csv('orders.csv', 50)
    print("Arquivo 'orders.csv' gerado com sucesso!")