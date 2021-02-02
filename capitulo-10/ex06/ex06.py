# Altere o programa de forma que a mensagem saldo insuficiente seja exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível

# Programa do livro, página 231
# from clientes import Cliente
# from contas import Conta
# joão = Cliente("João da Silva", "777-1234")
# maria = Cliente("Maria da Silva", "555-4321")
# conta1 = Conta([joão], 1, 1000)
# conta2 = Conta([maria, joão], 2, 500)
# conta1.saque(50)
# conta2.deposito(300)
# conta1.saque(190)
# conta2.deposito(95.15)
# conta2.saque(250)
# conta1.extrato()
# conta2.extrato()

from clients import Client
from account import Account

joao = Client('João da Silva', '777-1234')
maria = Client('Maria da Silva', '555-4321')

account1 = Account([joao], 1, 1000)
account2 = Account([maria, joao], 2, 500)

account1.withdraw(50)
account2.deposit(300)
account1.withdraw(2000)
account2.deposit(95.15)
account2.withdraw(250)
account1.extract()
account2.extract()
