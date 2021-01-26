# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte

initialDeposit = float(input('Depósito inicial: R$ '))
monthlyDeposit = float(input('Depósito mensal: R$ '))
interestRate = float(input('Taxa de juros da poupança (%): '))

month = 1
balance = initialDeposit

while month <= 24:
    balance += (balance * (interestRate / 100)) + monthlyDeposit
    print(f'{month:2}º mês = R$ {balance:.2f}')
    month += 1

print(f'\nO total ganho com juros no período foi de R$ {balance - initialDeposit:.2f}')

