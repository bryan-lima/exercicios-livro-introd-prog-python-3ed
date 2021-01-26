# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10

n = int(input('\nTabuada de: '))
start = int(input('De: '))
stop = int(input('Até: '))
x = start
while x <= stop:
    print(f'{n} x {x:2} = {n * x}')
    x += 1
