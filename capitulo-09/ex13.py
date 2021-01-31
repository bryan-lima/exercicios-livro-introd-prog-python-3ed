# Crie um programa que imprima as linhas de um arquivo
# Esse programa deve receber três parâmetros pela linha de comando:
# o nome do arquivo, a linha inicial e a última linha a imprimir

import sys

if len(sys.argv) != 4:
    print('\n\nUso: ex13.py arquivo inicio fim\n\n')
    sys.exit(1)

else:
    fileName = sys.argv[1]
    start = int(sys.argv[2])
    stop = int(sys.argv[3])

    try:
        with open(fileName, 'r', encoding='utf-8') as archive:
            for line in archive.readlines()[start - 1:stop]:
                print(line, end='')

    except Exception as error:
        print(f'\n\nOcorreu um erro: {error.args}')
    finally:
        archive.close()
