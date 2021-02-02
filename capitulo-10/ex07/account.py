from clients import Client


class Account:
    def __init__(self, clients, number, balance=0):
        self.balance = 0
        self.clients = clients
        self.number = number
        self.operations = []
        self.deposit(balance)

    def resume(self):
        print('-' * 30)
        print(f'CC Número: {self.number} Saldo: {self.balance:10.2f}')
        for client in self.clients:
            print(f'\nCliente: {client.name}\nTelefone: {client.phone}')
        print('-' * 30)

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.operations.append(['SAQUE', value])
        else:
            print(f'\nSaldo insuficiente!\n')

    def deposit(self, value):
        self.balance += value
        self.operations.append(['DEPÓSITO', value])

    def extract(self):
        print(f'Extrato CC Nº {self.number}\n')
        for operation in self.operations:
            print(f'{operation[0]:10s} {operation[1]:10.2f}')
        print(f'\n    Saldo: {self.balance:10.2f}\n')
