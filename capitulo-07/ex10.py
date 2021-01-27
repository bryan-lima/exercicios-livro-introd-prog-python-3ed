# Escreva um jogo da velha para dois jogadores
# O jogo deve perguntar onde você quer jogar e alternar entre os jogadores
# A cada jogada, verifique se a posição está livre
# Verifique também quando um jogador venceu a partida
# Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual cada elemento é outra lista, também com 3 elementos
# Exemplo do jogo:
#
#  X | O |
# ---+---+---
#    | X | X
# ---+---+---
#    |   | O
#
# Em que cada posição pode ser vista como um número
# Confira a seguir um exemplo das posições mapeadas para a mesma posição de seu teclado numérico
#
#  7 | 8 | 9
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  1 | 2 | 3
#

def line(size):
    print('-' * size)


game = [['', '', ''], ['', '', ''], ['', '', '']]

line(50)
print('JOGO DA VELHA' .center(50))
line(50)
print('COMO JOGAR: Para efetuar cada jogada, informe o\n'
      'número que corresponde ao local que deseja marcar.')
print('''
 7 | 8 | 9
---+---+---
 4 | 5 | 6
---+---+---
 1 | 2 | 3
''')
line(50)

playerX = int(input('JOGADOR X, digite a posição para marcar: '))
playerO = int(input('JOGADOR O, digite a posição para marcar: '))
