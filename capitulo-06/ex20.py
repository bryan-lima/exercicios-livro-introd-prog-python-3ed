# Escreva um programa que compare duas listas
# Considere a primeira lista como a versão inicial e a segunda como a versão após as alterações
# Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
# - os elementos que não mudaram
# - os novos elementos
# - os elementos que foram removidos

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

setA = set(a)
setB = set(b)

print(f'\nLista a: {a}')
print(f'Lista b: {b}')

print(f'\nElementos que não mudaram da lista a para lista b: {setA & setB}')
print(f'Novos elementos inseridos na lista b: {setB - setA}')
print(f'Elementos que foram removidos na lista b: {setA - setB}')
