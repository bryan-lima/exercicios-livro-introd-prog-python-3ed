# Crie um programa que gere uma página html com links para todos os arquivos jpg e png encontrados a partir de um
# diretório informado na linha de comando

import sys
import os.path
import urllib.request

if len(sys.argv) < 2:
    print('\n\nDigite o nome do diretório para coletar os arquivos jpg e png!')
    print('Uso: ex33.py diretório_com_imagens\n\n')
    sys.exit(1)

directory = sys.argv[1]

page = open('imagens.html', 'w', encoding='utf-8')
page.write('''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Imagens PNG e JPG</title>
</head>
<body>
''')
page.write(f'<h1>Imagens encontradas no diretório: {directory}</h1>')
for entry in os.listdir(directory):
    name, extension = os.path.splitext(entry)
    if extension in ['.jpg', '.png']:
        full_path = os.path.join(directory, entry)
        link = urllib.request.pathname2url(full_path)
        page.write(f'<p><a href="{link}" target= "_blank" rel="noreferrer noopener">{entry}</a></p>')

page.write('''
</body>
</html>
''')
page.close()
