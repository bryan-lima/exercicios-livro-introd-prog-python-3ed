# O que acontece se digitarmos 0 (zero) no valor a pagar?

# → Resposta: O programa funciona normalmente, imprimindo na tela 0 notas de R$ 50, e para logo em seguida.

# Programa 5.1 do livro, página 92
# Programa 5.1 - Contagem de cédulas

value = int(input('Digite o valor a pagar: '))
banknotes = 0
current = 50
payable = value

while True:
    if current <= payable:
        payable -= current
        banknotes += 1
    else:
        print(f'{banknotes} cédula(s) de R$ {current}')
        if payable == 0:
            break
        if current == 50:
            current = 20
        elif current == 20:
            current = 10
        elif current == 10:
            current = 5
        elif current == 5:
            current = 1
        banknotes = 0
