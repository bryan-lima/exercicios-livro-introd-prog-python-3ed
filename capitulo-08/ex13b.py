# Altere o Programa 8.20 de forma que o usuário tenha três chances de acertar o número
# O programa termina se o usuário acertar ou errar três vezes

# Programa 8.20 do livro, página 184
# Programa 8.20 - Adivinhando o número
#
# import random
#
# n = random.randint(1, 10)
# x = int(input('Escolha um número entre 1 e 10: '))
# if x == n:
#     print('Você acertou!')
# else:
#     print('Você errou.')

import random

numberRandom = random.randint(1, 10)
counter = 0

while True:
    chosenNumber = int(input('\nEscolha um número entre 1 e 10: '))
    counter += 1
    if chosenNumber == numberRandom:
        print(f'Parabéns! Você acertou na {counter}ª de 3 tentativas!')
        break
    else:
        print(f'Você errou!')
    if counter < 3:
        print(f'Resta(m) {3 - counter} tentativa(s).')
    else:
        print('Suas tentativas acabaram! Mais sorte na próxima vez.')
        print(f'O número sorteado foi {numberRandom}.')
        break
