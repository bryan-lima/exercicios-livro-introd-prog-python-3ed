# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios
# Calcule o preço a pagar de acordo com a tabela a seguir

def line(size):
    print('-' * size)


line(30)
print('ENERGIA ELÉTRICA' .center(30))
line(30)
consumption = int(input('Quantidade consumida de kWh: '))
installation = str(input('Tipo de instalação (R = Residência, I = Indústria ou C = Comércio): ')).strip()

if installation.upper()[0] == 'R':
    if consumption <= 500:
        price = 0.40
    else:
        price = 0.65
elif installation.upper()[0] == 'I':
    if consumption <= 1000:
        price = 0.55
    else:
        price = 0.60
elif installation.upper()[0] == 'C':
    if consumption <= 5000:
        price = 0.55
    else:
        price = 0.60
else:
    print('Tipo de instalação inválido!')

valuePayable = consumption * price
print(f'\nValor a pagar: R$ {valuePayable:.2f}')
