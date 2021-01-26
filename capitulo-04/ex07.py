# Rastreie o Programa 4.6
# Compare seu resultado ao apresentado na Tabela 4.2

# Programa 4.6 do livro, página 81
# Programa 4.6 - Categoria x preço

category = int(input('Digite a categoria do produto: '))

if category == 1:
    price = 10
else:
    if category == 2:
        price = 18
    else:
        if category == 3:
            price = 23
        else:
            if category == 4:
                price = 26
            else:
                if category == 5:
                    price = 31
                else:
                    print('Categoria inválida, digite um valor entre 1 e 5!')
                    price = 0

print(f'O preço do produto é: R$ {price:.2f}')
