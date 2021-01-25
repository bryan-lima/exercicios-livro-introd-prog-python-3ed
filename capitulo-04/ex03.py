# Escreva um programa que leia três números e que imprimam o maior e o menor

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
n3 = int(input('Informe mais um número inteiro: '))

bigger = n1
smaller = n1

if n2 > bigger:
    bigger = n2
if n3 > bigger:
    bigger = n3

if n2 < smaller:
    smaller = n2
if n3 < smaller:
    smaller = n3

print(f'\nO maior número informado é {bigger} e o menor número é {smaller}')
