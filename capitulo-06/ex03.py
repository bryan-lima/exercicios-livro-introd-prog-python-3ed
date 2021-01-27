# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos

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

firstAndSecondList = firstList + secondList
thirdList = []

counter = 0
while counter < len(firstAndSecondList):
    if firstAndSecondList[counter] not in thirdList:
        thirdList.append(firstAndSecondList[counter])
    counter += 1

print()
counter = 0
while counter < len(thirdList):
    print(f'{counter}: {thirdList[counter]}')
    counter += 1
