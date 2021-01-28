# Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo
# Valores esperados:
# múltiplo(8, 4) == True
# múltiplo(7, 3) == False
# múltiplo(5, 5) == True

def multiple(a, b):
    return a % b == 0


print(multiple(8, 4))
print(multiple(7, 3))
print(multiple(5, 5))
