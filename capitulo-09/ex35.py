# Utilizando a função os.walk, crie uma página HTML com o nome e tamanho de cada arquivo de um diretório passado e de
# seus subdiretórios

# Programa 9.10 do livro, página 219
# Programa 9.10 - Árvore de diretórios sendo percorrida
#
# import os
# import sys
#
# for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
#     print(f'\nCaminho:', raiz)
#     for d in diretorios:
#         print(f'  {d}/')
#     for f in arquivos:
#         print(f'  {f}/')
#     print(f'{len(diretorios)} diretório(s), {len(arquivos)} arquivo(s)')

import sys
import os
import os.path
import urllib.request


def generate_listing(page, directory):
    for root, directories, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)
            link = urllib.request.pathname2url(full_path)
            page.write(f"<p><a href='{link}'>{file}</a>  ({size} bytes)</p>")


if len(sys.argv) != 2:
    print('\n\nDigite o nome do diretório para coletar os arquivos!')
    print('Uso: ex35.py diretório\n\n')
    sys.exit(1)

directory = sys.argv[1]

page = open('diretorios-e-arquivos.html', 'w', encoding='utf-8')
page.write('''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Diretórios e Arquivos</title>
</head>
<body>
''')
page.write(f'<h1>Arquivos encontrados a partir do diretório: {directory}</h1>')
generate_listing(page, directory)
page.write('''
</body>
</html>
''')
page.close()
