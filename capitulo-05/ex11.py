# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança
# Exiba os valores mês a mês para 24 primeiros meses
# Escreva o total ganho com juros no período

initialDeposit = float(input('Depósito inicial: R$ '))
interestRate = float(input('Taxa de juros da poupança: '))

month = 1
balance = initialDeposit

while month <= 24:
    balance += (balance * (interestRate / 100))
    print(f'{month:2}º mês = R$ {balance:.2f}')
    month += 1

print(f'\nO total ganho com juros no período foi de R$ {balance - initialDeposit:.2f}')
