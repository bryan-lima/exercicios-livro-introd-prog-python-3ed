# Observe o método saque das classes Conta e ContaEspecial
# Modifique o método saque da classe Conta de forma que a verificação da possibilidade de saque seja feita por um novo
# método, substituindo a condição atual
# Esse novo método retornará verdadeiro se o saque puder ser efetuado, e falso, caso contrário
# Modifique a classe ContaEspecial de forma a trabalhar com esse novo método
# Verifique se você ainda precisa trocar o método saque da ContaEspecial ou apenas o novo método criado para verificar
# a possibilidade de saque

from clients import Client
from account import Account, SpecialAccount

jose = Client('José', '1243-3321')

account = SpecialAccount([jose], 3432, 5000, 1000)
account.extract()
account.withdraw(6000)
account.withdraw(3000)
account.withdraw(1000)
account.extract()
