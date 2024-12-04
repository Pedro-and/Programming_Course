from datetime import datetime, date

class ContaBancaria:
    def __init__(self, nome, numero_conta, tipo_conta):
        self.nome = nome
        self.numero_conta = numero_conta
        self.data_abertura = date.today()
        self.tipo_conta = tipo_conta
        self.saldo = 0.0
        self.movimentacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentacoes.append({
                'tipo': 'Depósito', 
                'valor': valor, 
                'data': datetime.now()
            })
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.movimentacoes.append({
                'tipo': 'Saque', 
                'valor': valor, 
                'data': datetime.now()
            })
            return True
        return False

    def extrato(self):
        print(f"\nExtrato da Conta {self.numero_conta}")
        print(f"Titular: {self.nome}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("\nMovimentações:")
        for mov in self.movimentacoes:
            print(f"{mov['data']} - {mov['tipo']}: R$ {mov['valor']:.2f}")

class GerenciadorContas:
    def __init__(self):
        self.contas = {}

    def cadastrar_conta(self, nome, numero_conta, tipo_conta):
        if numero_conta not in self.contas:
            nova_conta = ContaBancaria(nome, numero_conta, tipo_conta)
            self.contas[numero_conta] = nova_conta
            return nova_conta
        return None

    def editar_conta(self, numero_conta, novo_nome=None, novo_tipo=None):
        conta = self.contas.get(numero_conta)
        if conta:
            if novo_nome:
                conta.nome = novo_nome
            if novo_tipo:
                conta.tipo_conta = novo_tipo
            return True
        return False

    def excluir_conta(self, numero_conta):
        if numero_conta in self.contas:
            del self.contas[numero_conta]
            return True
        return False

    def obter_conta(self, numero_conta):
        return self.contas.get(numero_conta)

def main():
    gerenciador = GerenciadorContas()

    while True:
        print("\n--- Sistema de Gerenciamento Bancário ---")
        print("1. Cadastrar Nova Conta")
        print("2. Realizar Depósito")
        print("3. Realizar Saque")
        print("4. Visualizar Extrato")
        print("5. Editar Conta")
        print("6. Excluir Conta")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do correntista: ")
            numero_conta = input("Número da conta: ")
            tipo_conta = input("Tipo de conta (poupança/corrente): ")
            conta = gerenciador.cadastrar_conta(nome, numero_conta, tipo_conta)
            if conta:
                print("Conta cadastrada com sucesso!")
            else:
                print("Erro: Conta já existe.")

        elif opcao == '2':
            numero_conta = input("Número da conta: ")
            conta = gerenciador.obter_conta(numero_conta)
            if conta:
                valor = float(input("Valor do depósito: "))
                if conta.depositar(valor):
                    print("Depósito realizado com sucesso!")
                else:
                    print("Erro no depósito.")
            else:
                print("Conta não encontrada.")

        elif opcao == '3':
            numero_conta = input("Número da conta: ")
            conta = gerenciador.obter_conta(numero_conta)
            if conta:
                valor = float(input("Valor do saque: "))
                if conta.sacar(valor):
                    print("Saque realizado com sucesso!")
                else:
                    print("Saque não permitido.")
            else:
                print("Conta não encontrada.")

        elif opcao == '4':
            numero_conta = input("Número da conta: ")
            conta = gerenciador.obter_conta(numero_conta)
            if conta:
                conta.extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == '5':
            numero_conta = input("Número da conta: ")
            novo_nome = input("Novo nome (deixe em branco para manter): ")
            novo_tipo = input("Novo tipo de conta (deixe em branco para manter): ")
            if gerenciador.editar_conta(numero_conta, novo_nome, novo_tipo):
                print("Conta editada com sucesso!")
            else:
                print("Erro ao editar conta.")

        elif opcao == '6':
            numero_conta = input("Número da conta: ")
            if gerenciador.excluir_conta(numero_conta):
                print("Conta excluída com sucesso!")
            else:
                print("Erro ao excluir conta.")

        elif opcao == '7':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()