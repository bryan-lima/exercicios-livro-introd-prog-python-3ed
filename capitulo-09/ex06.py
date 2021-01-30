# Modifique o Programa 9.5 para imprimir 40 vezes o símbolo de = se este for o primeiro caractere da linha
# Adicione também a opção para parar de imprimir até que se pressione a tecla ENTER cada vez que uma linha iniciar
# com . (ponto) como primeiro caractere

# Programa 9.5 do livro, página 201
# Programa 9.5 - Processamento de um arquivo
#
# LARGURA = 79
#
# with open('entrada.txt') as entrada:
#     for linha in entrada.readlines():
#         if linha[0] == ';':
#             continue
#         elif linha[0] == '>':
#             print(linha[1:].rjust(LARGURA))
#         elif linha[0] == '*':
#             print(linha[1:].center(LARGURA))
#         else:
#             print(linha)

WIDTH = 79

with open('entrada.txt') as entry:
    for line in entry.readlines():
        if line[0] == ';':
            continue
        elif line[0] == '>':
            print(line[1:].rjust(WIDTH))
        elif line[0] == '*':
            print(line[1:].center(WIDTH))
        elif line[0] == '=':
            print('=' * 40)
        elif line[0] == '.':
            input('Digite algo para continuar')
            print()
        else:
            print(line)
