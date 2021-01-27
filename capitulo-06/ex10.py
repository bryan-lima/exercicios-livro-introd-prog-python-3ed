# Modifique o programa do Exercício 6.9 de forma a pesquisar p e v em toda a lista e informando o usuário a posição onde p e a posição onde v foram encontrados

L = [15, 7, 27, 39]
p = int(input('\nDigite o valor a procurar (p): '))
v = int(input('Digite o valor a procurar (v): '))

counter = 0
foundP = foundV = False
positionP = positionV = 0

while counter < len(L):
    if L[counter] == p and foundP is False:
        foundP = True
        positionP = counter
    if L[counter] == v and foundV is False:
        foundV = True
        positionV = counter
    counter += 1

if foundP:
    print(f'\nValor (p) {p} encontrado na posição {positionP}')
else:
    print(f'\nValor (p) {p} não encontrado')

if foundV:
    print(f'\nValor (v) {v} encontrado na posição {positionV}')
else:
    print(f'\nValor (v) {v} não encontrado')
