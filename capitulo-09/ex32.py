# Modifique o Programa 9.9 de forma a receber o nome do arquivo ou diretório a verificar pela linha de comando
# Imprima se existir e se for um arquivo ou um diretório

import sys
import os.path

if len(sys.argv) != 2:
    print('\n\nDigite o nome do arquivo ou diretório a verificar como parâmatro!')
    print('Uso: ex32.py nome\n\n')
    sys.exit(1)

name = sys.argv[1]

if os.path.isdir(name):
    print(f'{name}/')
    print(f'O diretório {name} existe')
elif os.path.isfile(name):
    print(f'{name}')
    print(f'O arquivo {name} existe')
else:
    print(f'{name} não existe')
