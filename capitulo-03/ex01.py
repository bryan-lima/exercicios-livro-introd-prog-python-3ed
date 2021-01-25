# Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado

def line(size):
    print('-' * size)


numbers = [5, 5.0, 4.3, -2, 100, 1.333]

line(30)
print(f'{"Número":^10} {"Tipo numérico":^20}')
for number in numbers:
    print(f'{number:^10} ', end="")
    if isinstance(number, int):
        print(f'{"Inteiro":^20}')
    elif isinstance(number, float):
        print(f'{"Ponto flutuante":^20}')
line(30)


