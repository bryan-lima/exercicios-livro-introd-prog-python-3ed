# Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre as palavras e no fim das linhas
# O arquivo de saída também não deve ter mais de uma linha em branco repetida

import sys

if len(sys.argv) != 3:
    print('\nUso: ex14.py entrada saida\n\n')
    sys.exit(1)

entry = sys.argv[1]
output = sys.argv[2]

fileEntry = open(entry, 'r', encoding='utf-8')
fileOutput = open(output, 'w', encoding='utf-8')
blankLine = 0

try:
    for line in fileEntry:
        line = line.rstrip()
        line = line.replace('  ', '')
        if line == '':
            blankLine += 1
        else:
            blankLine = 0
        if blankLine < 2:
            fileOutput.write(line + '\n')
except Exception as error:
    print(f'\n\nOcorreu um erro: {error.args}\n\n')
else:
    print(f'\n\nGerado arquivo "{output}"\nOperação finalizada com sucesso!\n\n')
finally:
    fileEntry.close()
    fileOutput.close()
