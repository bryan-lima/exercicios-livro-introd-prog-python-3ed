# Reescreva o Programa 5.1 de forma a continuar executando até que o valor digitado seja 0
# Utilize repetições aninhadas

while True:
    value = int(input('\nDigite o valor a pagar (0 para sair): '))

    if value == 0:
        break

    banknotes = 0
    current = 50
    payable = value

    while True:
        if current <= payable:
            payable -= current
            banknotes += 1
        else:
            print(f'{banknotes} cédula(s) de R$ {current}')
            if payable == 0:
                break
            if current == 50:
                current = 20
            elif current == 20:
                current = 10
            elif current == 10:
                current = 5
            elif current == 5:
                current = 1
            banknotes = 0

print('\nFim da execução!')
