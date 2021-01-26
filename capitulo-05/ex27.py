# Escreva um programa que verifique se um número é palíndromo
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos
# Exemplo: 454, 10501

num = input('\nDigite o número a verificar, sem espaços: ')

index = 0
lastIndex = len(num) - 1

while lastIndex > index and num[index] == num[lastIndex]:
    lastIndex -= 1
    index += 1

if num[index] == num[lastIndex]:
    print(f'{num} é palíndromo')
else:
    print(f'{num} não é palíndromo')
