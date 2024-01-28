class contaBancaria:

    def __init__(self, numeroConta, nome, saldo):
        self.numeroConta = numeroConta
        self.nome = nome
        self.saldo = saldo

    def depositar(self, quantia):
        self.saldo += quantia

    def sacar(self, quantia):
        self.saldo -= quantia

    def printInfoConta(self):
        print(f'''Numero da conta: {self.numeroConta}
Nome: {self.nome}
Saldo da conta: R${self.saldo:.2f}''')

contaVictor = contaBancaria(12337, 'Victor Galvão de Farias', 500.99)

contaVictor.printInfoConta()
