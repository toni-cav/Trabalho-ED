import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

def gerar_ordem_aleatoria(id_ordem: int, instante_atual: datetime):
    tipo = random.choice(("C", "V"))
    preco = round(random.uniform(10.0, 100.0), 2)
    quantidade = random.randint(1, 100) * 10
    novo_instante = instante_atual + timedelta(seconds=random.randint(1, 5))
    timestamp = novo_instante.strftime("%Y-%m-%d %H:%M:%S")
    return id_ordem, tipo, preco, quantidade, timestamp, novo_instante


def escrever_cabecalho_csv(writer):
    writer.writerow(["ID", "Type", "Price", "Quantity", "Timestamp"])


def gerar_ordens_csv(caminho_arquivo, quantidade_ordens: int):
    """Gera um CSV com a quantidade solicitada de ordens."""
    if quantidade_ordens <= 0:
        raise ValueError("A quantidade de ordens deve ser maior que zero.")

    caminho = Path(caminho_arquivo)
    caminho.parent.mkdir(parents=True, exist_ok=True)

    instante_atual = datetime.now()

    with caminho.open(mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        escrever_cabecalho_csv(writer)

        for id_ordem in range(1, quantidade_ordens + 1):
            id_ordem, tipo, preco, quantidade, timestamp, instante_atual = gerar_ordem_aleatoria(
                id_ordem,
                instante_atual,
            )
            writer.writerow([id_ordem, tipo, preco, quantidade, timestamp])


def gerar_multiplos_csv(diretorio_saida, quantidades):
    """Gera vários CSVs, um para cada quantidade informada."""
    diretorio = Path(diretorio_saida)
    diretorio.mkdir(parents=True, exist_ok=True)

    for quantidade in quantidades:
        gerar_ordens_csv(diretorio / f"orders_{quantidade}.csv", quantidade)


def main():
    try:
        texto = input("Digite as quantidades separadas por vírgula, exemplo 100,1000,5000: ")
        quantidades = tuple(int(item.strip()) for item in texto.split(",") if item.strip())
        gerar_multiplos_csv(Path(__file__).parent, quantidades)
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
    else:
        print("Arquivos gerados com sucesso.")


if __name__ == "__main__":
    main()