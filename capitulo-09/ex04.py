# Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando e que gere um arquivo de saída
# com as linhas do primeiro e do segundo arquivo

def readFile(file):
    line = file.readline()
    if line == '':
        return None
    else:
        return line


def writeFile(file, content):
    file.write(content)


import sys

if len(sys.argv) != 3:
    print('\nUso: ex04.py primeiro_arquivo.txt segundo_arquivo.txt\n\n')
else:
    firstParam = sys.argv[1]
    secondParam = sys.argv[2]

    firstFile = open(firstParam, 'r')
    secondFile = open(secondParam, 'r')
    firstAndSecondUnited = open(f'{firstParam}+{secondParam}.txt', 'w')

    try:
        while True:
            firstContent = readFile(firstFile)
            if firstContent is None:
                break
            writeFile(firstAndSecondUnited, firstContent)

        while True:
            secondContent = readFile(secondFile)
            if secondContent is None:
                break
            writeFile(firstAndSecondUnited, secondContent)
    except Exception as error:
        print(f'\n\nOcorreu um erro: {error.args}')
    else:
        print(f'\n\nFoi gerado o arquivo "{firstParam}+{secondParam}.txt".\nOperação finalizada com sucesso!')
    finally:
        firstFile.close()
        secondFile.close()
        firstAndSecondUnited.close()
