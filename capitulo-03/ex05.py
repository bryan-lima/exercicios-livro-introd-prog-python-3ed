# Calcule o resultado da expressão A > B and C or D, utilizando os valores da tabela a seguir

def line(size):
    print('-' * size)


line(4 * 7 + 11)
print(f'{"A":^7}{"B":^7}{"C":^7}{"D":^7} Resultado')
line(4 * 7 + 11)
A = 1
B = 2
C = True
D = False
print(f'{A:^7}{B:^7}{C:^7}{D:^7} {A > B and C or D}')  # False

A = 10
B = 3
C = False
D = False
print(f'{A:^7}{B:^7}{C:^7}{D:^7} {A > B and C or D}')  # False

A = 5
B = 1
C = True
D = True
print(f'{A:^7}{B:^7}{C:^7}{D:^7} {A > B and C or D}')  # True
line(4 * 7 + 11)
