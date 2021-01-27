# Modifique o Programa 6.6 usando for
# Explique por que nem todos os while podem ser transformados em for

# → Resposta: O primeiro while do Programa 6.6 não pode ser convertido pois não se sabe
# a quantidade de números que será informado pelo usuário

# Programa 6.6 do livro, página 104
# Programa 6.6 - Adição de elementos à lista
#
# L = []
#
# while True:
#     n = int(input('Digite um número (0 para sair): '))
#     if n == 0:
#         break
#     L.append(n)
#
# x = 0
# while x < len(L):
#     print(L[x])
#     x += 1

L = []

print()
while True:
    n = int(input('Digite um número (0 para sair): '))
    if n == 0:
        break
    L.append(n)

print(f'\nOs números digitados foram:')
for e in L:
    print(e)
