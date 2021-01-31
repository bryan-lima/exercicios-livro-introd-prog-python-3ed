# Modifique o programa do Exercício 9.11 para também registrar a linha e a coluna de cada ocorrência da palavra no arquivo
# Para isso, utilize listas nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência

import sys

if len(sys.argv) != 2:
    print('\n\nUso: ex11.py arquivo\n\n')
    sys.exit(1)

else:
    fileName = sys.argv[1]
    fileDict = {}
    cLine = 1
    column = 1

    with open(fileName, 'r', encoding='utf-8') as archive:
        for line in archive:
            line = line.strip().lower()
            words = line.split(" ")
            for w in words:
                if w == "":
                    column += 1
                    continue
                if w in fileDict:
                    fileDict[w].append((cLine, column))
                else:
                    fileDict[w] = [(cLine, column)]
                column += len(w) + 1
            cLine += 1
            column = 1

        for key, value in fileDict.items():
            print(f'{key} = {value}')
