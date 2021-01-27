# Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável achou
# Dica: observe a condição de saída do while

# Programa 6.9 do livro, página 110
# Programa 6.9 - Pesquisa Sequencial

L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))

counter = 0

while counter < len(L):
    if L[counter] == p:
        print(f'{p} encontrado na posição {counter}')
        break
    counter += 1
    if counter == len(L):
        print(f'{p} não encontrado')
