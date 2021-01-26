# Modifique o programa para também trabalhar com notas de R$ 100

value = int(input('Digite o valor a pagar: '))
banknotes = 0
current = 100
payable = value

while True:
    if current <= payable:
        payable -= current
        banknotes += 1
    else:
        print(f'{banknotes} cédula(s) de R$ {current}')
        if payable == 0:
            break
        if current == 100:
            current = 50
        elif current == 50:
            current = 20
        elif current == 20:
            current = 10
        elif current == 10:
            current = 5
        elif current == 5:
            current = 1
        banknotes = 0
