# Crie um programa que receba uma lista de nomes de arquivo e os imprima, um por um

# fileList = ['ex01.py', 'ex02.py', 'ex03.py']
#
# for file in fileList:
#     with open(file, 'r', encoding='utf-8') as archive:
#         print(f'\nARQUIVO: {file + " ":-<91}')
#         for line in archive.readlines():
#             print(line[:-1])
#         print()
#         print('-' * 100)

import sys

if len(sys.argv) < 2:
    print("\nUso: ex09.py arquivo1 arquivo2 arquivo3 arquivoN\n\n")
    sys.exit(1)

for file in sys.argv[1:]:
    with open(file, 'r', encoding='utf-8') as archive:
        print(f'\nARQUIVO: {file + " ":-<91}')
        for line in archive:
            print(line, end='')
        print()
        print('-' * 100)
