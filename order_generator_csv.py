import csv
import random
from datetime import datetime, timedelta


def generate_orders_csv(filename, num_orders):
    order_types = ['C', 'V']
    current_time = datetime.now()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Type', 'Price', 'Quantity', 'Timestamp'])
        for i in range(1, num_orders + 1):
            order_id = i
            order_type = random.choice(order_types)
            price = round(random.uniform(10.0, 100.0), 2)
            # Quantidade de cada lotes de ações de 10 a 1000
            quantity = random.randint(1, 100) * 10
            # Timestamp Adiciona de 1 a 5 segundos de intervalo entre as ordens
            current_time += timedelta(seconds=random.randint(1, 5))
            timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([order_id, order_type, price, quantity, timestamp])


if __name__ == "__main__":
    try:
        quantidade_arquivos = int(input("Digite a quantidade de arquivos que deseja gerar: "))
    except ValueError:
        print("\nEntrada inválida! Por favor, digite apenas números inteiros.")
    else:
        if quantidade_arquivos <= 0:
            print("\nPor favor, digite um número maior que zero.")
        else:
            # Loop para gerar a quantidade de arquivos solicitada,
            for i in range(1, quantidade_arquivos + 1):
                try:
                    quantidade_ordens = int(
                        input(f"Digite a quantidade de ordens para o arquivo {i} de {quantidade_arquivos}: ")
                    )
                except ValueError:
                    print(f"\nEntrada inválida para o arquivo {i}. Esse arquivo não será gerado.\n")
                    continue

                if quantidade_ordens <= 0:
                    print(f"\nQuantidade inválida para o arquivo {i} (deve ser maior que zero). "
                          f"Esse arquivo não será gerado.\n")
                    continue

                nome_arquivo = f'orders_{i}.csv'
                generate_orders_csv(nome_arquivo, quantidade_ordens)
                print(f"Arquivo '{nome_arquivo}' gerado com {quantidade_ordens} ordens!\n")

            print("Processo finalizado com sucesso!")
