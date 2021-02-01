# Altere o Programa 7.2, o jogo da forca
# Dessa vez, utilize as funções de tempo para cronometrar a duração das partidas

import time
import sys
import random

FILE_SCOREBOARD = 'placar.txt'
FILE_WORDS_LIST = 'palavras.txt'

wordsList = []
scoreboardDict = {}


def load_words():
    try:
        file = open(FILE_WORDS_LIST, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f'\n\nArquivo "{FILE_WORDS_LIST}" não encontrado!')
        print(f'Para jogar, crie um arquivo de palavras com nome "{FILE_WORDS_LIST}", contendo uma palavra por linha.\n\n')
        sys.exit(1)
    for word in file.readlines():
        word = word.strip().lower()
        if word != '':
            wordsList.append(word)
    file.close()


def load_scoreboard():
    try:
        file = open(FILE_SCOREBOARD, 'r+')
    except FileNotFoundError:
        file = open(FILE_SCOREBOARD, 'w+')
    for line in file.readlines():
        line = line.strip()
        if line != '':
            user, counter = line.split(';')
            scoreboardDict[user] = int(counter)
    file.close()


def save_scoreboard():
    file = open(FILE_SCOREBOARD, 'w', encoding='utf-8')
    for user in scoreboardDict.keys():
        file.write(f'{user};{scoreboardDict[user]}\n')
    file.close()


def update_scoreboard(user):
    if user in scoreboardDict:
        scoreboardDict[user] += 1
    else:
        scoreboardDict[user] = 1
    save_scoreboard()


def show_scoreboard():
    scoreboardOrdered = []
    for user, score in scoreboardDict.items():
        scoreboardOrdered.append([user, score])
    scoreboardOrdered.sort(key=lambda score: score[1])
    print('\n\nMelhores jogadores por número de acertos:')
    scoreboardOrdered.reverse()
    for up in scoreboardOrdered:
        print(f'{up[0]:30s} {up[1]:10d}')


load_words()
load_scoreboard()

word = wordsList[random.randint(0, len(wordsList)-1)]

typed = []
hits = []
errors = 0

start = time.time()

while True:
    password = ''

    for letter in word:
        password += letter if letter in hits else '_'
    print(password)

    if password == word:
        stop = time.time()
        print('Você acertou!')
        name = input('Digite seu nome: ')
        update_scoreboard(name)
        break

    attempt = input('\nDigite uma letra: ').lower().strip()

    if attempt in typed:
        print('Você já tentou esta letra!')
        continue
    else:
        typed += attempt
        if attempt in word:
            hits += attempt
        else:
            errors += 1
            print('Você errou!')

    print('X==:==\nX  :   ')
    print('X  O   ' if errors >= 1 else 'X')

    line2 = ''
    if errors == 2:
        line2 = r'  |   '
    elif errors == 3:
        line2 = r' \|   '
    elif errors >= 4:
        line2 = r' \|/ '
    print(f'X{line2}')

    line3 = ''
    if errors == 5:
        line3 += r' /     '
    elif errors >= 6:
        line3 += r' / \ '
    print(f'X{line3}')

    print('X\n===========')

    if errors == 6:
        print('Enforcado!')
        break

show_scoreboard()
print(f'\nDuração da partida {stop - start} segundos')
