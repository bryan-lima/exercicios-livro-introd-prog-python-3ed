# Modifique o exemplo para pesquisar dois valores
# Em vez de apenas p, leia outro valor v que também será procurado
# Na impressão, indique qual dos dois valores foi achado primeiro

L = [15, 7, 27, 39]
p = int(input('\nDigite o primeiro valor a procurar: '))
v = int(input('Digite o segundo valor a procurar: '))

foundFirst = 0
foundP = foundV = False
counter = 0

while counter < len(L):
    if L[counter] == p and foundP is False:
        foundP = True
        if foundFirst == 0:
            foundFirst = p
    if L[counter] == v and foundV is False:
        foundV = True
        if foundFirst == 0:
            foundFirst = v
    counter += 1

if foundP:
    print(f'\n{p} encontrado!')
else:
    print(f'\n{p} não encontrado!')

if foundV:
    print(f'\n{v} encontrado!')
else:
    print(f'\n{v} não encontrado!')
print(f'\nO primeiro número encontrado foi {foundFirst}')
