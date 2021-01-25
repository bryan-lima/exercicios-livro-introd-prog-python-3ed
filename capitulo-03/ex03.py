# Complete a tabela a seguir utilizando a = True, b = False e c = True

def line(size):
    print('-' * size)


a = True
b = False
c = True

line(20)
print(' Expressão  Resultado')
print(f'{"a and a":^11} {a and a}')  # True
print(f'{"b and b":^11} {b and b}')  # False
print(f'{"not c":^11} {not c}')  # False
print(f'{"not b":^11} {not b}')  # True
print(f'{"not a":^11} {not a}')  # False
print(f'{"a and b":^11} {a and b}')  # False
print(f'{"b and c":^11} {b and c}')  # False
print(f'{"a or c":^11} {a or c}')  # True
print(f'{"b or c":^11} {b or c}')  # True
print(f'{"c or a":^11} {c or a}')  # True
print(f'{"c or b":^11} {c or b}')  # True
print(f'{"c or c":^11} {c or c}')  # True
print(f'{"b or b":^11} {b or b}')  # False
line(20)
