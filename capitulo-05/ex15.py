# Escreva um programa para controlar uma pequena máquina registradora
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada
# Utilize a tabela de códigos a seguir para obter o preço de cada produto
#  ________________
# | Código | Preço |
# |   1    | 0,50  |
# |   2    | 1,00  |
# |   3    | 4,00  |
# |   5    | 7,00  |
# |   9    | 8,00  |
#  ----------------
# Seu programa deve exibir o total das compras depois que o usuário digitar 0
# Qualquer outro código deve gerar a mensagem de  erro "Código inválido"

def line(size):
    print('-' * size)


line(50)
print('MÁQUINA REGISTRADORA' .center(50))
line(50)
valuePayable = 0
while True:
    productCode = int(input('\nDigite o código do produto (0 para sair): '))
    price = 0
    if productCode == 0:
        line(50)
        break
    elif productCode == 1:
        price = 0.50
    elif productCode == 2:
        price = 1
    elif productCode == 3:
        price = 4
    elif productCode == 5:
        price = 7
    elif productCode == 9:
        price = 8
    else:
        print('Código inválido!')
    if price != 0:
        quantity = int(input('Quantidade comprada: '))
        valuePayable += quantity * price
    line(50)


print(f'O valor total das compras é de R$ {valuePayable:.2f}' .center(50))
line(50)
