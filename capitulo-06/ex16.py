# Modifique o Programa 6.20 para ordenar a lista em ordem decrescente
# L = [1, 2, 3, 4, 5] deve ser ordenada como L = [5, 4, 3, 2, 1]

L = [1, 2, 3, 4, 5]
print(f'\nLista original (antes da ordenação decrescente): {L}')

end = 5

while end > 1:
    changed = False
    index = 0
    while index < end - 1:
        if L[index] < L[index + 1]:
            changed = True
            temp = L[index]
            L[index] = L[index + 1]
            L[index + 1] = temp
        index += 1
    if not changed:
        break
    end -= 1

print('\nLista depois da ordenação decrescente: ')
for e in L:
    print(e)
