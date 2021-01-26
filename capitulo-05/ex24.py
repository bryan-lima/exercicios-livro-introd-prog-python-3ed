# Modifique o programa anterior de forma a ler um número n
# Imprima os n primeiros números primos

while True:
    n = int(input('\nDigite um número inteiro: '))
    if n < 0:
        print('Opção inválida! Permitido apenas números positivos.')
    if n >= 0:
        break

if n >= 1:
    if n == 1:
        print(f'O primeiro número primo é:')
    else:
        print(f'Os {n} primeiros números primos são: ')
    print('2')
    cousinCounter = 1
    y = 3
    while cousinCounter < n:
        x = 3
        while x < y:
            if y % x == 0:
                break
            x += 2
        if x == y:
            print(x)
            cousinCounter += 1
        y = y + 2
