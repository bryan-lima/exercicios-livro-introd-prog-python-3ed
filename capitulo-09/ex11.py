# Crie um programa que leia um arquivo e crie um dicionário em que cada chave é uma palavra e cada valor é o número
# de ocorrências no arquivo

import sys

if len(sys.argv) != 2:
    print('\n\nUso: ex11.py arquivo\n\n')
    sys.exit(1)

else:
    fileName = sys.argv[1]
    fileDict = {}

    with open(fileName, 'r', encoding='utf-8') as archive:
        for line in archive:
            line = line.strip().lower()
            words = line.split()
            for word in words:
                if word in fileDict:
                    fileDict[word] += 1
                else:
                    fileDict[word] = 1

        for key, value in fileDict.items():
            print(f'{key} = {value}')
