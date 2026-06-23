from src.data_structures.node import Node
from src.data_structures.queue import Queue
from src.data_structures.stack import Stack
from src.data_structures.ordem import Ordem
from src.data_structures.linked_list import Linked_List_Compra, Linked_List_Venda

class Motor_Match:

    def __init__(self):
        self.lista_compras = Linked_List_Compra()
        self.lista_vendas = Linked_List_Venda()
        self.fila_entrada = Queue()   # Fila FIFO de entrada de novas ordens
        self.pilha_undo = Stack()     # Pilha com IDs inseridos com sucesso no livro
        self.transacoes = []

    def inserir_ordem(self, ordem: Ordem):
        """
        Ponto de entrada de uma nova ordem no sistema.
        Toda ordem nova entra primeiro na fila FIFO, aguardando
        ser processada pelo motor (Seção 3.2 do enunciado).
        """
        self.fila_entrada.enfileirar(ordem)

    def processar_fila(self):
        """
        Processa, em ordem de chegada (FIFO), todas as ordens
        que estão atualmente na fila de entrada.
        """
        while not self.fila_entrada.esta_vazia():
            ordem = self.fila_entrada.desenfileirar()
            self.processar_ordem(ordem)

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
            # Registra no undo apenas a ordem que efetivamente passou
            # a repousar no livro de ofertas
            self.pilha_undo.enfileirar(('C', ordem_compra.id))

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
            # Registra no undo apenas a ordem que efetivamente passou
            # a repousar no livro de ofertas
            self.pilha_undo.enfileirar(('V', ordem_venda.id))

    def desfazer_ultima_acao(self):
        """
        Sistema de Undo, desfaz a última
        inserção bem-sucedida no livro de ofertas, removendo a
        ordem correspondente através do seu ID.
        """
        if self.pilha_undo.esta_vazia():
            print("Não há ações para desfazer.")
            return None

        tipo, id_ordem = self.pilha_undo.desenfileirar()

        if tipo == 'C':
            ordem_removida = self.lista_compras.remover_por_id(id_ordem)
        else:
            ordem_removida = self.lista_vendas.remover_por_id(id_ordem)

        if ordem_removida is not None:
            print(f"[UNDO] Ordem ID {id_ordem} ({tipo}) removida do livro.")
        else:
            # Pode acontecer se a ordem já tiver sido total ou
            # parcialmente casada após sua inserção no livro
            print(
                f"[UNDO] Ordem ID {id_ordem} ({tipo}) não encontrada "
                f"no livro (provavelmente já foi casada)."
            )

        return ordem_removida

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