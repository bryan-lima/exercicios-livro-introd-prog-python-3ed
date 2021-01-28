# Utilizando a função type, escreva uma função recursiva que imprima os elementos de uma lista
# Cada elemento deve ser impresso separadamente, um por linha
# Considere o caso de listas dentro de listas, como L = [1, [2, 3, 4, [5, 6, 7]]]
# A cada nível, imprima a lista mais à direita, como fazemos para indentar blocos em Python
# Dica: envie o nível atual como parâmetro e utilize-o para calcular a quantidade de espaços em branco à esquerda de cada elemento

SPACES_BY_LEVEL = 4


def print_elements(lst, level=0):
    spaces = ' ' * SPACES_BY_LEVEL * level
    if type(lst) == list:
        print(spaces, '[')
        for e in lst:
            print_elements(e, level + 1)
        print(spaces, ']')
    else:
        print(spaces, lst)


L = [1, [2, 3, 4, [5, 6, 7]]]

print_elements(L)
