# Modifique o programa do Exercício 9.7 para também receber o número de caracteres por linha e o número de linhas por
# página pela linha de comando

# Programa testado com Moby Dick: http://www.gutenberg.org/cache/epub/2701/pg2701.txt
# Gravado com o nome de mobydick.txt

import sys

if len(sys.argv) != 4:
    print('\nUso: ex08.py arquivo caracteres_por_linha linhas_por_página')
    print('\nExemplo: ex08.py mobydick.txt 76 60\n'
          '→ Define saída paginada do arquivo "mobydick.txt" com 76 caracteres por linhas e 60 linhas por página')
    sys.exit(1)

else:
    FILE_NAME = sys.argv[1]
    WIDTH = int(sys.argv[2])
    LINES = int(sys.argv[3])


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

    try:
        page = 1
        lines = 1

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
    finally:
        entry.close()
        output.close()
