from clients import Client


class Account:
    def __init__(self, clients, number, balance=0):
        self.balance = 0
        self.clients = clients
        self.number = number
        self.operations = []
        self.deposit(balance)

    def resume(self):
        print('-' * 34)
        print(f'CC Número: {self.number} Saldo: {self.balance:10.2f}')
        for client in self.clients:
            print(f'\nCliente: {client.name}\nTelefone: {client.phone}')
        print('-' * 34)

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.operations.append(['SAQUE', value])
            return True
        else:
            print(f'\nSaldo insuficiente!\n')
            return False

    def deposit(self, value):
        self.balance += value
        self.operations.append(['DEPÓSITO', value])

    def extract(self):
        print(f'Extrato CC Nº {self.number}\n')
        for operation in self.operations:
            print(f'{operation[0]:10s} {operation[1]:10.2f}')
        print(f'\n    Saldo: {self.balance:10.2f}\n')


class SpecialAccount(Account):
    def __init__(self, clients, number, balance=0, limit=0):
        Account.__init__(self, clients, number, balance)
        self.limit = limit

    def withdraw(self, value):
        if self.balance + self.limit >= value:
            self.balance -= value
            self.operations.append(['SAQUE', value])
            return True
        else:
            return Account.withdraw(self, value)

    def extract(self):
        Account.extract(self)
        print(f'    Limite: {self.limit:9.2f}')
        print(f'Disponível: {self.limit + self.balance:9.2f}\n')
