# Escreva uma função que retorne o maior de dois números
# Valores esperados:
# máximo(5, 6) == 6
# máximo(2, 1) == 2
# máximo(7, 7) == 7

def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


print(maximum(5, 6))
print(maximum(2, 1))
print(maximum(7, 7))
