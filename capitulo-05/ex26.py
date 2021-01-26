# Escreva um programa que calcule o resto da divisão inteira entre dois números
# Utilize apenas as operações de soma e subtração para calcular o resultado

dividend = int(input('Dividendo: '))
divider = int(input('Divisor: '))

n = dividend

while n >= divider:
    n -= divider
rest = n
print(f"{dividend} / {divider} = {rest} (resto)")
