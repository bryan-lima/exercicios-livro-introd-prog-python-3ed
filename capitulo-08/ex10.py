# Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão

def fibonacci(n):
    a = 0
    b = 1
    while n > 0:
        a, b = b, b + a
        n -= 1
    return a


num = int(input('Digite um número para cálculo da sequência de Fibonacci: '))

for i in range(num):
    print(f"fibonacci({i}) = {fibonacci(i)}")
