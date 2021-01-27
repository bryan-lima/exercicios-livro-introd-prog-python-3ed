# Escreva um programa que compare duas listas
# Utilizando operações com conjuntos, imprima:
# - os valores comuns às duas listas
# - os valores que só existem na primeira
# - os valores que existem apenas na segunda
# - uma lista com os elementos não repetidos das duas listas
# - a primeira lista sem os elementos repetidos na segunda

a = [1, 2, 3, 4, 5]
b = [5, 3, 7, 8, 1]

print(f'\nLista a = {a}')
print(f'Lista b = {b}')

setA = set(a)
setB = set(b)

print(f'\nValores comuns às duas listas: {setA & setB}')
print(f'Valores que só existem na primeira: {setA - setB}')
print(f'Valores que só existem na segunda: {setB - setA}')
print(f'Lista com os elementos não repetidos das duas listas: {setA - setB | setB - setA}')
print(f'Primeira lista sem os elementos repetidos na segunda: {setA - setB}')
