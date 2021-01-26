# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair
# Imprima a tabuada da operação escolhida
# Repita até que a opção saída seja escolhida

def line(size):
    print('-' * size)


while True:
    print()
    line(30)
    print('MENU' .center(30))
    line(30)
    print(' 1 - Adição')
    print(' 2 - Subtração')
    print(' 3 - Divisão')
    print(' 4 - Multiplicação')
    print(' 5 - Sair')
    line(30)
    option = int(input('Escolha uma opção: '))
    if option == 5:
        break
    elif 1 <= option < 5:
        n = int(input('Tabuada de: '))
        x = 1
        while x <= 10:
            if option == 1:
                print(f'{n} + {x:2} = {n + x}')
            elif option == 2:
                print(f'{n} - {x:2} = {n - x}')
            elif option == 3:
                print(f'{n} / {x:2} = {n / x:.2f}')
            elif option == 4:
                print(f'{n} x {x:2} = {n * x}')
            x += 1
    else:
        print('Opção inválida!')

print('\nFim da execução!')
