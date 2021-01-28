# Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprima todas linhas desse arquivo

import sys

if len(sys.argv) != 2:
    print('\nUso: ex01.py nome_do_arquivo\n\n')
else:
    file = sys.argv[1]

    try:
        with open(file, 'r') as archive:
            for line in archive.readlines():
                print(line[:-1])
    except Exception as error:
        print(f'Houve um erro: {error.args[1]}')
