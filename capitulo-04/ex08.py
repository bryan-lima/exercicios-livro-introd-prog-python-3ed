# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/)
# Exiba o resultado da operação solicitada

def line(size):
    print('-' * size)


line(34)
print('CALCULADORA BÁSICA' .center(34))
line(34)
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
line(34)
option = str(input('Digite a operação (+,-,* ou /): '))

if option == '+':
    result = n1 + n2
elif option == '-':
    result = n1 - n2
elif option == '*':
    result = n1 * n2
elif option == '/':
    result = n1 / n2
else:
    print('Opção inválida!')

print(f'\nResultado: {result:.1f}')
