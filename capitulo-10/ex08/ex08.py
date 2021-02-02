# crie uma nova conta, agora tendo João e José como clientes e saldo igual a 500

from clients import Client
from account import Account

joao = Client('João da Silva', '777-1234')
maria = Client('Maria da Silva', '555-4321')
jose = Client('José Soares', '333-2143')

account1 = Account([joao], 1, 1000)
account2 = Account([maria, joao], 2, 500)
account3 = Account([joao, jose], 3, 500)

account1.resume()
account2.resume()
account3.resume()
