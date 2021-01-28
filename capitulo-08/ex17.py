# Escreva um generator capaz e gerar a série de Fibonacci

def fibonacci(n):
    p = 0
    s = 1
    while n > 0:
        yield s
        p, s = s, s + p
        n -= 1


for x in fibonacci(20):
    print(x)
