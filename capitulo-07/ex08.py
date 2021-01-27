# Modifique o Programa 7.2 de forma a utilizar uma lista de palavras
# No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula:
# índice = (número * 776) % len(lista_de_palavras)

words = ['casa', 'bola', 'mangueira', 'uva', 'quiabo', 'computador', 'cobra', 'lentilha', 'arroz',
         'macaco', 'pudim', 'café']

index = int(input('Digite um numero: '))
word = words[(index * 776) % len(words)]

# word = str(input('Digite a palavra secreta: ')).lower().strip()

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
