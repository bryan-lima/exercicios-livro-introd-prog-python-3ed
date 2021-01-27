# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras

firstList = []
secondList = []

print()
while True:
    n = int(input('Digite um número para a primeira lista (0 para terminar): '))
    if n == 0:
        break
    firstList.append(n)

print()
while True:
    n = int(input('Digite um número para a segunda lista (0 para sair): '))
    if n == 0:
        break
    secondList.append(n)

thirdList = firstList + secondList
counter = 0

print()
while counter < len(thirdList):
    print(f"{counter}: {thirdList[counter]}")
    counter += 1
