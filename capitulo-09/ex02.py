# Modifique o programa do Exercício 9.1 para que receba mais dois parâmetros: a linha de início e a de fim para impressão
# O programa deve imprimir apenas as linhas entres esses dois valores (incluindo as linhas de início e fim)

import sys

if len(sys.argv) != 4:
    print('\nUso: ex01.py nome_do_arquivo linha_inicio linha_fim\n\n')
else:
    file = sys.argv[1]
    start = int(sys.argv[2])
    stop = int(sys.argv[3])

    try:
        with open(file, 'r') as archive:
            for line in archive.readlines()[start-1:stop]:
                print(line[:-1])
    except Exception as error:
        print(f'\nHouve um erro: {error.args[1]}')
