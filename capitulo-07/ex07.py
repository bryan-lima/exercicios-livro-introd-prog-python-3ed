# Modifique o jogo da forca (Programa 7.2) de forma a escrever a palavra secreta caso o jogador perca

# Programa 7.2 do livro, página 154
# Programa 7.2 - Jogo da forca

word = str(input('Digite a palavra secreta: ')).lower().strip()

for x in range(100):
    print()

typed = []
hits = []
errors = 0

while True:
    password = ''

    for letter in word:
        password += letter if letter in hits else '.'
    print(password)

    if password == word:
        print('Você acertou!')
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

    print('X==:==\nX  :  ')
    print('X  O  ' if errors >= 1 else 'X')

    line2 = ''

    if errors == 2:
        line2 = r'  |  '
    elif errors == 3:
        line2 = r' \|  '
    elif errors >= 4:
        line2 = r' \|/ '
    print(f'X{line2}')

    line3 = ''

    if errors == 5:
        line3 += r' /   '
    elif errors >= 6:
        line3 += r' / \ '
    print(f'X{line3}')
    print('X\n===========')

    if errors == 6:
        print('\nEnforcado!')
        print(f'A palavra secreta era: {word}')
        break
