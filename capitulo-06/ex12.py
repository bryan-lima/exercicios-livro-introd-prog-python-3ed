# Altere o Programa 6.11 de forma a imprimir o menor elemento da lista

# Programa 6.11 do livro, página 114
# Programa 6.11 - Verificação do maior valor
#
# L = [1, 7, 2, 4]
# maximo = L[0]
# for e in L:
#     if e > maximo:
#         maximo = e
# print(maximo)

L = [1, 7, 2, 4]

minimum = L[0]

for e in L:
    if e < minimum:
        minimum = e

print(f'\nA lista L possui os valores: {L}')
print(f'O menor valor da lista é {minimum}')
