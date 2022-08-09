class ContaCorrente:
    total_contas = 0

    def __init__(self):
        self.numero_conta = 0
        self.titular = ''
        self.saldo = 0.0

    def criar_conta(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

        ContaCorrente.total_contas += 1

    def imprimir_dados(self):
        print(f'Número da conta: {self.numero_conta}')
        print(f'Titular: {self.titular}')
        print(f'Saldo {self.saldo}\n')


cliente1 = ContaCorrente()
cliente2 = ContaCorrente()
cliente3 = ContaCorrente()

cliente1.criar_conta(100, 'Ana', 75.00)
cliente2.criar_conta(200, 'Pedro', 120.00)
cliente3.criar_conta(300, 'Maria', 150.00)

cliente1.imprimir_dados()
cliente2.imprimir_dados()
cliente3.imprimir_dados()

print('Total de contas cadastradas:', ContaCorrente.total_contas)
