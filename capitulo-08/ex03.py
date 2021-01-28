# Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²)
# Valores esperados:
# área_quadrado(4) == 16
# área_quadrado(9) == 81

def squareArea(side):
    return side ** 2


print(f'Área do quadrado de lado 4: {squareArea(4)}')
print(f'Área do quadrado de lado 9: {squareArea(9)}')
