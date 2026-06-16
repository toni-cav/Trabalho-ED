from src.data_structures.node import Node
from src.data_structures.ordem import Ordem
from src.data_structures.linked_list import Linked_List_Compra, Linked_List_Venda


class Motor_Match:

    def __init__(self):
        self.lista_compras = Linked_List_Compra()
        self.lista_vendas = Linked_List_Venda()
        self.transacoes = []

    def processar_ordem(self, ordem: Ordem):
        if ordem.tipo == 'C':
            self.processar_compra(ordem)

        elif ordem.tipo == 'V':
            self.processar_venda(ordem)

        else:
            print("Tipo de ordem inválido.")

    def processar_compra(self, ordem_compra: Ordem):
        """
        Uma compra casa com vendas quando:

        preço_compra >= preço_venda
        """

        while (
            ordem_compra.quantidade > 0
            and self.lista_vendas.inicio is not None
            and ordem_compra.preco >= self.lista_vendas.inicio.data.preco
        ):
            melhor_venda = self.lista_vendas.inicio.data

            quantidade_negociada = min(
                ordem_compra.quantidade,
                melhor_venda.quantidade
            )

            preco_negociado = melhor_venda.preco

            self.registrar_transacao(
                id_compra=ordem_compra.id,
                id_venda=melhor_venda.id,
                preco=preco_negociado,
                quantidade=quantidade_negociada
            )

            ordem_compra.quantidade -= quantidade_negociada
            melhor_venda.quantidade -= quantidade_negociada

            if melhor_venda.quantidade == 0:
                self.lista_vendas.remover_inicio()

        if ordem_compra.quantidade > 0:
            no_compra = Node(ordem_compra)
            self.lista_compras.adicionar_no(no_compra)

    def processar_venda(self, ordem_venda: Ordem):
        """
        Uma venda casa com compras quando:

        preço_compra >= preço_venda
        """

        while (
            ordem_venda.quantidade > 0
            and self.lista_compras.inicio is not None
            and self.lista_compras.inicio.data.preco >= ordem_venda.preco
        ):
            melhor_compra = self.lista_compras.inicio.data

            quantidade_negociada = min(
                melhor_compra.quantidade,
                ordem_venda.quantidade
            )

            preco_negociado = melhor_compra.preco

            self.registrar_transacao(
                id_compra=melhor_compra.id,
                id_venda=ordem_venda.id,
                preco=preco_negociado,
                quantidade=quantidade_negociada
            )

            melhor_compra.quantidade -= quantidade_negociada
            ordem_venda.quantidade -= quantidade_negociada

            if melhor_compra.quantidade == 0:
                self.lista_compras.remover_inicio()

        if ordem_venda.quantidade > 0:
            no_venda = Node(ordem_venda)
            self.lista_vendas.adicionar_no(no_venda)

    def registrar_transacao(self, id_compra, id_venda, preco, quantidade):
        transacao = {
            "id_compra": id_compra,
            "id_venda": id_venda,
            "preco": preco,
            "quantidade": quantidade
        }

        self.transacoes.append(transacao)

        print(
            f"Transação realizada | "
            f"Compra ID {id_compra} | "
            f"Venda ID {id_venda} | "
            f"Preço R$ {preco:.2f} | "
            f"Qtd {quantidade}"
        )

    def imprimir_livro(self):
        print("\n========== LIVRO DE OFERTAS ==========")

        print("\nCOMPRAS")
        print(self.lista_compras.imprimir())

        print("\nVENDAS")
        print(self.lista_vendas.imprimir())

        print("\n======================================")

    def imprimir_transacoes(self):
        print("\n========== TRANSAÇÕES ==========")

        if len(self.transacoes) == 0:
            print("Nenhuma transação realizada.")
            return

        for transacao in self.transacoes:
            print(
                f"Compra ID {transacao['id_compra']} | "
                f"Venda ID {transacao['id_venda']} | "
                f"Preço R$ {transacao['preco']:.2f} | "
                f"Qtd {transacao['quantidade']}"
            )