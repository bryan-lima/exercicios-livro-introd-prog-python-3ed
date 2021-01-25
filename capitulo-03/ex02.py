# Complete a tabela a seguir, respondendo True ou False
# Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5

def line(size):
    print('-' * size)


a = 4
b = 10
c = 5.0
d = 1
f = 5

line(26)
print(f'{"Expressão":^12} {"Resultado"}')
result = a == c
print(f'{"a == c":^12} {result}')

result = a < b
print(f'{"a < b":^12} {result}')

result = d > b
print(f'{"d > b":^12} {result}')

result = c != f
print(f'{"c != f":^12} {result}')

result = a == b
print(f'{"a == b":^12} {result}')

result = c < d
print(f'{"c < d":^12} {result}')

result = b > a
print(f'{"a == c":^12} {result}')

result = c >= f
print(f'{"c >= f":^12} {result}')

result = f >= c
print(f'{"f >= c":^12} {result}')

result = c <= c
print(f'{"c <= c":^12} {result}')

result = c <= f
print(f'{"c <= f":^12} {result}')
line(26)

