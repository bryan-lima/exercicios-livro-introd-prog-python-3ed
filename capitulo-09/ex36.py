# Utilizando a função os.walk, crie um programa que calcule o espaço ocupado por cada diretório e subdiretório, gerando
# uma página html com os resultados

import sys
import os
import os.path
import math


def size_for_human(size):
    if size == 0:
        return '0 byte'
    greatness = math.log(size, 10)
    if greatness < 3:
        return f'{size} bytes'
    elif greatness < 6:
        return f'{size / 1024.0:7.3f} KB'
    elif greatness < 9:
        return f'{size / pow(1024, 2)} MB'
    elif greatness < 12:
        return f'{size / pow(1024, 3)} GB'


style_mask = '"margin: 5px 0px 5px %dpx;"'


def generate_style(level):
    return style_mask % (level * 30)


def generate_level_and_style(root):
    def level(path):
        xlevel = path.count(os.sep) - nroot
        return generate_style(xlevel)
    nroot = root.count(os.sep)
    return level


def generate_listing(page, directory):
    directory = os.path.abspath(directory)
    indenter = generate_level_and_style(directory)
    stack = [[directory, 0]]
    for root, directories, files in os.walk(directory):
        while not root.startswith(stack[-1][0]):
            last = stack.pop()
            page.write(f'<p style={indenter(last[0])}>Tamanho: ({size_for_human(last[1])})</p>')
            stack[-1][1] += last[1]
        page.write(f'<p style={indenter(root)}>{root}</p>')
        directory_size = 0
        for file in files:
            full_path = os.path.join(root, file)
            directory_size += os.path.getsize(full_path)
        stack.append([root, directory_size])
    while len(stack) > 1:
        last = stack.pop()
        page.write(f'<p style={indenter(last[0])}>Tamanho: ({size_for_human(last[1])})</p>')
        stack[-1][1] += last[1]


if len(sys.argv) < 2:
    print('Digite o nome do diretório para coletar os arquivos!')
    sys.exit(1)

directory = sys.argv[1]

page = open('tamanho-dir-e-arq.html', 'w', encoding='utf-8')
page.write('''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
''')
page.write(f'Arquivos encontrados a partir do diretório: {directory}')
generate_listing(page, directory)
page.write('''
</body>
</html>
''')
page.close()
