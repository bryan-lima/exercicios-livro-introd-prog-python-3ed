# Crie um programa que corrija o Programa 9.9 de forma a verificar se z existe e é um diretório

# Programa 9.9 do livro, página 214
# Programa 9.9 - Verificação se um diretório ou arquivo já existe
#
# import os.path
#
# if os.path.exists('z'):
#     print('O diretório z existe')
# else:
#     print('O diretório z não existe')

import os.path

if os.path.isdir('z'):
    print('O diretório z existe!')
elif os.path.isfile('z'):
    print('z existe, mas é um arquivo e não um diretório')
else:
    print('O diretório z não existe')
