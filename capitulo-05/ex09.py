# Escreva um programa que leia dois números
# Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão
# Utilize apenas os operadores de soma e subtração para calcular o resultado
# Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo
# Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20

dividend = int(input('Dividendo: '))
divider = int(input('Divisor: '))

quotient = 0
n = dividend

while n >= divider:
    n -= divider
    quotient += + 1
rest = n
print(f"{dividend} / {divider} = {quotient} (quociente) {rest} (resto)")
