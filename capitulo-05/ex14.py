# Escreva um programa que leia números inteiros do teclado
# O programa deve ler os números até que o usuário digite 0 (zero)
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética

counter = 0
summation = 0

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 0:
        break
    summation += n
    counter += 1

print(f'\nQuantidade de números digitados: {counter}')
print(f'Soma: {summation}')
print(f'Média: {summation / counter:.2f}')
