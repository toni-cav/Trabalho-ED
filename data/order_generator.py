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
    try:
        quantidade_ordens = int(input("Digite a quantidade de ordens que deseja gerar: ")) #Quantidade de ordens
        quantidade_arquivos = int(input("Digite a quantidade de arquivos que deseja gerar: ")) #Quantidade de arquivos csv
        
        if quantidade_ordens <= 0 or quantidade_arquivos <= 0:
            print("\nPor favor, digite números maiores que zero.")
        else:
            # Loop para gerar a quantidade de arquivos solicitada
            for i in range(1, quantidade_arquivos + 1):
                nome_arquivo = f'orders_{i}.csv'
                
                # Chama a função passando o nome e a quantidade de ordens
                generate_orders_csv(nome_arquivo, quantidade_ordens)
                print(f"Arquivo '{nome_arquivo}' gerado com {quantidade_ordens} ordens!")
            
            print("\nProcesso finalizado com sucesso!")
            
    except ValueError:
        print("\nEntrada inválida! Por favor, digite apenas números inteiros.")