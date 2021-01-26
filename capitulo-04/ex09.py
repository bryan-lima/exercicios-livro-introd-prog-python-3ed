# Escreva um programa para aprovar um empréstimo bancário para compra de uma casa
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar
# O valor da prestação mensal não pode ser superior a 30% do salário
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar

def line(size):
    print('-' * size)


line(30)
print('EMPRÉSTIMO BANCÁRIO' .center(30))
line(30)
houseValue = float(input('Valor da casa: R$ '))
buyerSalary = float(input('Salário do comprador: R$ '))
financingYears = int(input('Quantos anos de financiamento? '))

financingValue = houseValue / (financingYears * 12)
thirtyPercentSalary = (buyerSalary / 100) * 30

print(f'\nPara pagar uma casa de R$ {houseValue:.2f} em {financingYears} anos, a prestação será de R$ {financingValue:.2f}.')

if financingValue <= thirtyPercentSalary:
    print('\nEmpréstimo pode ser CONCEDIDO!')
else:
    print('\nEmpréstimo NEGADO!')
