# Altere a classe ContaEspecial de forma que seu extrato exiba o limite e o total disponível para saque

from clients import Client
from account import Account, SpecialAccount

jose = Client('José', '1243-3321')

account = SpecialAccount([jose], 3432, 50000, 10000)
account.extract()


