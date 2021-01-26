# O que acontece se digitarmos 0,001 no programa anterior?
# Caso ele não funcione, altere-o de forma a corrigir o problema

# → Resposta: O programa para de executar após imprimir 0 notas de R$ 100

value = float(input('Digite o valor a pagar: '))
banknotes = 0
current = 100
payable = value

while True:
    if current <= payable:
        payable -= current
        banknotes += 1
    else:
        if current >= 1:
            print(f'{banknotes} cédula(s) de R$ {current}')
        else:
            print(f'{banknotes} moedas de R$ {current:.2f}')
        if payable < 0.01:
            break
        if current == 100:
            current = 50
        elif current == 50:
            current = 20
        elif current == 20:
            current = 10
        elif current == 10:
            current = 5
        elif current == 5:
            current = 1
        elif current == 1:
            current = 0.50
        elif current == 0.50:
            current = 0.10
        elif current == 0.10:
            current = 0.05
        elif current == 0.05:
            current = 0.02
        elif current == 0.02:
            current = 0.01
        banknotes = 0

