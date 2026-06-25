from datetime import datetime

from src.data_structures.motor_match import Motor_Match
from src.models.ordem import Ordem


class AplicacaoLivroOfertas:
    """Controla a interação do usuário com o motor de negociação."""

    def __init__(self):
        self.motor = Motor_Match()
        self.proximo_id = 1
        self.rodando = True

    @staticmethod
    def _linha():
        print("=" * 78)

    @staticmethod
    def _formatar_horario(timestamp):
        """Exibe timestamps numéricos de forma legível no terminal."""
        try:
            return datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")
        except (TypeError, ValueError, OSError, OverflowError):
            return str(timestamp)

    @staticmethod
    def _ler_texto(mensagem):
        while True:
            try:
                texto = input(mensagem).strip()
            except EOFError:
                raise SystemExit("\nEntrada encerrada. Simulação finalizada.")

            if texto:
                return texto

            print("Entrada vazia. Tente novamente.")

    def _ler_inteiro_positivo(self, mensagem):
        while True:
            texto = self._ler_texto(mensagem)

            try:
                valor = int(texto)
            except ValueError:
                print("Digite um número inteiro válido.")
                continue

            if valor <= 0:
                print("Digite um valor maior que zero.")
                continue

            return valor

    def _ler_preco_positivo(self, mensagem):
        while True:
            texto = self._ler_texto(mensagem).replace(",", ".")

            try:
                valor = float(texto)
            except ValueError:
                print("Digite um preço válido, por exemplo: 12,50.")
                continue

            if valor <= 0:
                print("O preço deve ser maior que zero.")
                continue

            return valor

    def _ler_tipo_ordem(self):
        while True:
            tipo = self._ler_texto("Tipo [C]ompra / [V]enda: ").upper()

            if tipo == "C" or tipo == "V":
                return tipo

            print("Tipo inválido. Digite C para compra ou V para venda.")

    def _enfileirar_ordem(self, tipo, preco, quantidade):
        """Cria uma ordem com ID único e a envia para a fila de entrada."""
        ordem = Ordem(
            id_ordem=self.proximo_id,
            tipo=tipo,
            preco=preco,
            quantidade=quantidade,
        )

        self.motor.inserir_ordem(ordem)
        self.proximo_id += 1
        return ordem

    def _imprimir_lista_ordens(self, titulo, estrutura, descricao_vazia):
        self._linha()
        print(titulo)
        self._linha()

        if estrutura.esta_vazia():
            print(descricao_vazia)
            return

        print(f"{'Pos.':>4} | {'ID':>4} | {'Tipo':^4} | {'Preço (R$)':>12} | {'Quantidade':>10} | Entrada")
        print("-" * 78)

        atual = estrutura.inicio
        posicao = 1

        while atual is not None:
            ordem = atual.data
            horario = self._formatar_horario(ordem.timestamp)
            print(
                f"{posicao:>4} | {ordem.id:>4} | {ordem.tipo:^4} | "
                f"{ordem.preco:>12.2f} | {ordem.quantidade:>10} | {horario}"
            )
            atual = atual.next
            posicao += 1

        print("-" * 78)
        print(f"Total de ordens nesta estrutura: {estrutura.tamanho}")

    def _imprimir_pilha_undo(self):
        self._linha()
        print("HISTÓRICO DE UNDO (topo para a base)")
        self._linha()

        if self.motor.pilha_undo.esta_vazia():
            print("Nenhuma ordem repousando no livro pode ser desfeita.")
            return

        atual = self.motor.pilha_undo.topo
        posicao = 1

        while atual is not None:
            marcador = "<- próxima a ser desfeita" if posicao == 1 else ""
            print(f"{posicao:>4}. Ordem ID {atual.data} {marcador}")
            atual = atual.next
            posicao += 1

        print(f"Total de ações registradas: {self.motor.pilha_undo.tamanho}")

    def _imprimir_resumo(self):
        self._linha()
        print("RESUMO DA SIMULAÇÃO")
        self._linha()
        print(f"Ordens aguardando na fila: {self.motor.fila_entrada.tamanho}")
        print(f"Ordens de compra no livro: {self.motor.lista_compras.tamanho}")
        print(f"Ordens de venda no livro:  {self.motor.lista_vendas.tamanho}")
        print(f"Transações realizadas:      {self.motor.lista_transacoes.tamanho}")
        print(f"Ações disponíveis para undo: {self.motor.pilha_undo.tamanho}")

    def exibir_painel(self):
        print()
        self._imprimir_resumo()
        print()
        self._imprimir_lista_ordens(
            "FILA DE ENTRADA — ordem FIFO de processamento",
            self.motor.fila_entrada,
            "Não há ordens aguardando processamento.",
        )
        print()
        self._imprimir_lista_ordens(
            "LIVRO DE OFERTAS — COMPRAS (melhor preço no início)",
            self.motor.lista_compras,
            "Não há ordens de compra no livro.",
        )
        print()
        self._imprimir_lista_ordens(
            "LIVRO DE OFERTAS — VENDAS (melhor preço no início)",
            self.motor.lista_vendas,
            "Não há ordens de venda no livro.",
        )
        print()
        self._imprimir_pilha_undo()

    def exibir_transacoes(self):
        self._linha()
        print("HISTÓRICO DE TRANSAÇÕES")
        self._linha()

        if self.motor.lista_transacoes.esta_vazia():
            print("Nenhuma transação foi realizada até o momento.")
            return

        print(f"{'Nº':>4} | {'Compra':>7} | {'Venda':>6} | {'Preço (R$)':>12} | {'Quantidade':>10} | Horário")
        print("-" * 78)

        atual = self.motor.lista_transacoes.inicio
        posicao = 1

        while atual is not None:
            transacao = atual.data
            horario = self._formatar_horario(transacao.timestamp)
            print(
                f"{posicao:>4} | {transacao.id_compra:>7} | {transacao.id_venda:>6} | "
                f"{transacao.preco:>12.2f} | {transacao.quantidade:>10} | {horario}"
            )
            atual = atual.next
            posicao += 1

        print("-" * 78)
        print(f"Total de transações: {self.motor.lista_transacoes.tamanho}")

    def inserir_ordem_manual(self):
        self._linha()
        print("NOVA ORDEM")
        self._linha()
        print(f"O sistema atribuirá automaticamente o ID {self.proximo_id}.")

        tipo = self._ler_tipo_ordem()
        preco = self._ler_preco_positivo("Preço unitário (R$): ")
        quantidade = self._ler_inteiro_positivo("Quantidade: ")

        ordem = self._enfileirar_ordem(tipo, preco, quantidade)

        print()
        print(
            f"Ordem ID {ordem.id} enfileirada com sucesso: "
            f"{ordem.tipo} | R$ {ordem.preco:.2f} | {ordem.quantidade} unidades."
        )
        print("Ela será processada quando a opção 'Processar fila' for escolhida.")

    def processar_fila(self):
        if self.motor.fila_entrada.esta_vazia():
            print("\nA fila de entrada está vazia. Não há ordens para processar.")
            return

        quantidade = self.motor.fila_entrada.tamanho
        print(f"\nProcessando {quantidade} ordem(ns) em ordem FIFO...")
        self.motor.processar_fila()
        print("Processamento concluído.")
        self._imprimir_resumo()

    def desfazer_ultima_acao(self):
        print()
        ordem_removida = self.motor.desfazer_ultima_acao()

        if ordem_removida is not None:
            print(
                f"Ordem removida: ID {ordem_removida.id} | {ordem_removida.tipo} | "
                f"R$ {ordem_removida.preco:.2f} | {ordem_removida.quantidade} unidades."
            )

    def carregar_cenario_demonstracao(self):
        """Reinicia a sessão e monta um cenário que evidencia fila, match e undo."""
        self.motor = Motor_Match()
        self.proximo_id = 1

        self._enfileirar_ordem("V", 100.00, 90)
        self._enfileirar_ordem("V", 101.50, 50)
        self._enfileirar_ordem("C", 99.50, 70)
        self._enfileirar_ordem("C", 102.00, 120)
        self._enfileirar_ordem("V", 98.50, 100)

        print()
        print("Cenário de demonstração carregado e reiniciado.")
        print("Foram enfileiradas 5 ordens. Use 'Processar fila' para executar o motor.")

    def reiniciar_simulacao(self):
        confirmacao = self._ler_texto("Digite S para confirmar o reinício completo: ").upper()

        if confirmacao != "S":
            print("Reinício cancelado.")
            return

        self.motor = Motor_Match()
        self.proximo_id = 1
        print("Simulação reiniciada. O próximo ID será 1.")

    def exibir_menu(self):
        print()
        self._linha()
        print("SIMULADOR DE LIVRO DE OFERTAS")
        self._linha()
        print("1 - Inserir nova ordem na fila")
        print("2 - Processar fila de entrada")
        print("3 - Exibir painel completo")
        print("4 - Exibir histórico de transações")
        print("5 - Desfazer última inserção no livro")
        print("6 - Carregar cenário de demonstração")
        print("7 - Reiniciar simulação")
        print("0 - Encerrar")
        self._linha()

    def executar(self):
        print("\nBem-vindo ao simulador de livro de ofertas.")
        print("Todas as ordens entram primeiro na fila FIFO antes de chegar ao motor.")

        while self.rodando:
            self.exibir_menu()
            opcao = self._ler_texto("Escolha uma opção: ")

            if opcao == "1":
                self.inserir_ordem_manual()
            elif opcao == "2":
                self.processar_fila()
            elif opcao == "3":
                self.exibir_painel()
            elif opcao == "4":
                self.exibir_transacoes()
            elif opcao == "5":
                self.desfazer_ultima_acao()
            elif opcao == "6":
                self.carregar_cenario_demonstracao()
            elif opcao == "7":
                self.reiniciar_simulacao()
            elif opcao == "0":
                self.rodando = False
            else:
                print("Opção inválida. Escolha um número do menu.")

        print("\nSimulação encerrada. Até logo!")


def main():
    """Ponto de entrada da aplicação."""
    aplicacao = AplicacaoLivroOfertas()

    try:
        aplicacao.executar()
    except KeyboardInterrupt:
        print("\n\nSimulação encerrada pelo usuário.")


if __name__ == "__main__":
    main()
