# Rastreie o Programa 8.6 e compare o seu resultado com o apresentado

# → Resposta: O programa calcula o fatorial de 4, o qual é calculado usando chamadas recursivas

# Programa 8.6 do livro, página 167
# Programa 8.6 - Função modificada para facilitar o rastreamento

def factorial(n):
    print(f'Calculando o fatorial de {n}')
    if n == 0 or n == 1:
        print(f'Fatorial de {n} = 1')
        return 1
    else:
        fat = n * factorial(n - 1)
        print(f'Fatorial de {n} = {fat}')
    return fat


factorial(4)
