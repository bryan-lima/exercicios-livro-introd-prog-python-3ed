# Crie um programa que receba uma lista de nome de arquivos e que gere apenas um grande arquivo de saída

import sys

FILE_NAME = 'join-files.txt'

if len(sys.argv) < 2:
    print('\nUso: ex10.py arquivo1 arquivo2 arquivo3 arquivoN\n\n')
    sys.exit(1)

output = open(FILE_NAME, 'w', encoding='utf-8')

try:
    for file in sys.argv[1:]:
        with open(file, 'r', encoding='utf-8') as archive:
            output.write(f'ARQUIVO: {file} ' .ljust(100, '-') + '\n')
            for line in archive:
                output.write(line)
            output.write(f'-' * 100 + '\n')
except Exception as error:
    print(f'\n\nOcorreu um erro: {error.args}\n')
else:
    print(f'\n\nGerado arquivo "{FILE_NAME}".\nOperação finalizada com sucesso!\n')
finally:
    output.close()
