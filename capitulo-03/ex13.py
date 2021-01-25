# Escreva um programa que converta uma temperatura digitada em ºC em ºF
# A fórmula para essa conversão é F = ((9 x C) / 5) + 32

def line(size):
    print('-' * size)


line(50)
print('CONVERSOR DE TEMPERATURA' .center(50))
line(50)
print('De Celsius (ºC) para Fahrenheit (ºF)' .center(50))
line(50)
celsius = int(input('\nInforme a temperatura em ºC: '))
fahrenheit = (9 * celsius / 5) + 32
print(f'\n{celsius}ºC equivale a {fahrenheit:.1f}ºF')
line(50)
