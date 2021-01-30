# Crie um programa que leia os arquivos pares.txt e ímpares.txt e que crie um só arquivo pareseimpares.txt com
# todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica

# Para gerar os arquivos pares.txt e impares.txt, execute:
#
# with open('pares.txt', 'w') as pairs, open('impares.txt', 'w') as odds:
#     for i in range(0, 1001):
#         if i % 2 == 0:
#             pairs.write(f'{i}\n')
#         else:
#             odds.write(f'{i}\n')

def readNumber(file):
    while True:
        number = file.readline()
        if number == '':
            return None
        if number.strip() != '':
            return int(number)


def writeNumber(file, number):
    file.write(f'{number}\n')


pairs = open('pares.txt', 'r')
odds = open('impares.txt', 'r')
pairsAndOdds = open('pareseimpares.txt', 'w')

nPair = readNumber(pairs)
nOdd = readNumber(odds)

while True:
    if nPair is None and nOdd is None:
        break
    if nPair is not None and (nOdd is None or nPair <= nOdd):
        writeNumber(pairsAndOdds, nPair)
        nPair = readNumber(pairs)
    if nOdd is not None and (nPair is None or nOdd <= nPair):
        writeNumber(pairsAndOdds, nOdd)
        nOdd = readNumber(odds)

pairs.close()
odds.close()
pairsAndOdds.close()

print(f'\nFim da execução!')
