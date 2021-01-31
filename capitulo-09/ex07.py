# Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado
# Cada linha não deve conter mais de 76 caracteres
# Cada página terá no máximo 60 linhas
# Adicione na última linha de cada página o número da página atual e o nome do arquivo original

# Programa testado com Moby Dick: http://www.gutenberg.org/cache/epub/2701/pg2701.txt
# Gravado com o nome de mobydick.txt

WIDTH = 76
LINES = 60
FILE_NAME = 'mobydick.txt'


def checkPage(file, line, page):
    if line == LINES:
        footer = f'= {FILE_NAME} - Página: {page} ='
        file.write(footer.center(WIDTH - 1) + '\n')
        page += 1
        line = 1
    return line, page


def write(file, line, nLines, page):
    file.write(line + '\n')
    return checkPage(file, nLines + 1, page)


entry = open(FILE_NAME, encoding='utf-8')
output = open(f'{FILE_NAME}__Saida-Paginada.txt', 'w', encoding='utf-8')

page = 1
lines = 1

try:
    for line in entry.readlines():
        words = line.rstrip().split(' ')
        line = ''
        for w in words:
            w = w.strip()
            if len(line) + len(w) + 1 > WIDTH:
                lines, page = write(output, line, lines, page)
                linha = ''
            line += w + ' '
        if line != '':
            lines, page = write(output, line, lines, page)

    while lines != 1:
        lines, pagina = write(output, '', lines, page)
except Exception as error:
    print(f'\nOcorreu um erro: {error.args[1]}')
else:
    print(f'\nGerado arquivo "{FILE_NAME}__Saida-Paginada.txt".\nOperação finalizada com sucesso!')

entry.close()
output.close()
