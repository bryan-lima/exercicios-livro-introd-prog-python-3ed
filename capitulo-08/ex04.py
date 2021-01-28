# Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura) / 2)
# Valores esperados
# área_triângulo(6, 9) == 27
# área_triângulo(5, 8) == 20

def triangleArea(base, height):
    return (base * height) / 2


print(f'Área do triângulo: 6 x 9 = {triangleArea(6, 9)}')
print(f'Área do triângulo: 5 x 8 = {triangleArea(5, 8)}')
