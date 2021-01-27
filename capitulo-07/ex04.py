# Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string
# String: TTAAC
# Resultado:
# T: 2x
# A: 2x
# C: 1x

# Minha solução inicial
# string = str(input('\nDigite uma string: '))
# compare = ''
#
# for letter in string:
#     if letter not in compare:
#         compare += letter
#         print(f'{letter}: {string.count(letter)}x')

string = str(input('\nDigite uma string: '))
counter = {}

for letter in string:
    counter[letter] = counter.get(letter, 0) + 1

for key, value in counter.items():
    print(f'{key}: {value}x')
