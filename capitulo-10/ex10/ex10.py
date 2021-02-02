# Modifique as classes Conta e ContaEspecial para que a operação de saque retorne verdadeiro se o saque foi efetuado
# e falso, caso contrário

from clients import Client
from account import Account, SpecialAccount

joao = Client('João', '5554-3322')
jose = Client('José', '1243-3321')

account1 = Account([joao, jose], 2341, 500)
account1.resume()
print(account1.withdraw(1000))
print(account1.withdraw(100))
account1.resume()

account2 = SpecialAccount([jose], 3432, 50000, 10000)
account2.resume()
print(account2.withdraw(100000))
print(account2.withdraw(500))
account2.resume()