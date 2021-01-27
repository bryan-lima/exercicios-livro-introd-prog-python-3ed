# Modifique o Programa 7.2 para utilizar listas de strings para desenhar o boneco da forca
# Você pode utilizar uma lista para cada linha e organizá-las em uma lista de listas
# Em vez de controlar quando imprimir cada parte, desenhe nessas listas, substituindo o elemento a desenhar
# Exemplo:
# >>> linha = list('X------')
# >>> linha
# ['X', '-', '-', '-', '-', '-', '-']
# >>> linha[6] = '|'
# >>> linha
# >>> ''.join(linha)
# 'X-----|'

words = ['casa', 'bola', 'mangueira', 'uva', 'quiabo', 'computador', 'cobra', 'lentilha', 'arroz',
         'macaco', 'pudim', 'café']

index = int(input('Digite um numero: '))
word = words[(index * 776) % len(words)]

for x in range(100):
    print()

typed = []
hits = []
errors = 0

lines_txt = """
X==:==
X  :
X    
X    
X    
X    
=======

"""

lines = []

for line in lines_txt.splitlines():
    lines.append(list(line))

while True:
    password = ''

    for letra in word:
        password += letra if letra in hits else '.'
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
            if errors == 1:
                lines[3][3] = 'O'
            elif errors == 2:
                lines[4][3] = '|'
            elif errors == 3:
                lines[4][2] = '\\'
            elif errors == 4:
                lines[4][4] = '/'
            elif errors == 5:
                lines[5][2] = '/'
            elif errors == 6:
                lines[5][4] = '\\'

    for l in lines:
        print(''.join(l))

    if errors == 6:
        print('Enforcado!')
        print(f'A palavra secreta era: {word}')
        break
