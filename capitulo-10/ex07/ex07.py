# Modifique o método resumo da classe Conta para exibir o nome e telefone de cada cliente

from clients import Client
from account import Account

joao = Client('João da Silva', '777-1234')
maria = Client('Maria da Silva', '555-4321')

account1 = Account([joao], 1, 1000)
account2 = Account([maria, joao], 2, 500)

account1.resume()
account2.resume()
