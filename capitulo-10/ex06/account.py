# Programa 10.1 do livro, página 230
# Programa 10.1 – Conta com registro de operações e extrato (contas.py)
#
# class Conta:
#     def __init__(self, clientes, número, saldo=0):
#         self.saldo = 0
#         self.clientes = clientes
#         self.número = número
#         self.operações = []
#         self.deposito(saldo)
#
#     def resumo(self):
#         print(f"CC N°{self.número} Saldo: {self.saldo:10.2f}")
#
#     def saque(self, valor):
#         if self.saldo >= valor:
#             self.saldo -= valor
#             self.operações.append(["SAQUE", valor])
#
#     def deposito(self, valor):
#         self.saldo += valor
#         self.operações.append(["DEPÓSITO", valor])
#
#     def extrato(self):
#         print(f"Extrato CC N° {self.número}\n")
#         for o in self.operações:
#             print(f"{o[0]:10s} {o[1]:10.2f}")
#         print(f"\n    Saldo: {self.saldo:%10.2f}\n")

class Account:
    def __init__(self, clients, number, balance=0):
        self.balance = 0
        self.clients = clients
        self.number = number
        self.operations = []
        self.deposit(balance)

    def resume(self):
        print(f'CC Número: {self.number} Saldo: {self.balance:10.2f}')

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
