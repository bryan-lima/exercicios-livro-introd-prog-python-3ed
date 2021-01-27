# Altere o Programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida
# Verifique se o nome do produto digitado existe no dicionário, e só então efetue a baixa em estoque

# Programa 6.22 do livro, página 128
# Programa 6.22 - Exemplo de dicionário com estoque e operações de venda
#
# estoque = {'tomate': [1000, 2.30],
#            'alface': [500, 0.45],
#            'batata': [2001, 1.20],
#            'feijao': [100, 1.50]}
# venda = [['tomate', 5], ['batata', 10], ['alface', 5]]
# total = 0
# print('Vendas:\n')
# for operacao in venda:
#     produto, quantidade = operacao
#     preco = estoque[produto][1]
#     custo = preco * quantidade
#     print(f'{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
#     estoque[produto][0] -= quantidade
#     total += custo
# print(f' Custo total: {total:21.2f}\n')
# print('Estoque:\n')
# for chave, dados in estoque.items():
#     print('Descrição: ', chave)
#     print('Quantidade: ', dados[0])
#     print(f'Preço: {dados[1]:6.2f}\n')

def line(size):
    print('-' * size)


stock = {'TOMATE': [1000, 2.30],
         'ALFACE': [500, 0.45],
         'BATATA': [2001, 1.20],
         'FEIJAO': [100, 1.50]}

endList = len(stock)

counter = 0
line(40)
print('ESTOQUE ATUAL' .center(40))
line(40)
for key, data in stock.items():
    counter += 1
    print(f'{"Descrição":<20} {key}')
    print(f'{"Quantidade":<20} {data[0]}')
    print(f'{"Preço":<20} {data[1]:.2f}')
    if counter != endList:
        print()
line(40)

# sale = [['tomate', 5], ['batata', 10], ['alface', 5]]

sale = []

while True:
    saleProduct = str(input('\nDigite o nome do produto (fim para sair): ')).strip().upper()
    if saleProduct == 'FIM':
        break
    if saleProduct in stock:
        saleQuantity = int(input(f'Quantidade de {saleProduct} comprada: '))
        try:
            sale.append([saleProduct, saleQuantity])
        except:
            print(f'Houve um erro ao tentar adicionar o produto {saleProduct} ao carrinho.')
            print('Por favor, tente novamente!')
        else:
            print(f'Adicionado {saleQuantity} unidades de {saleProduct} ao carrinho com sucesso!')
    else:
        print(f'Desculpe, infelizmente não temos o produto {saleProduct} no estoque.')

total = 0

print()
line(40)
print('VENDAS' .center(40))
line(40)
print(f'{"PRODUTO":<15} {"UN.":>4} {"PREÇO":>8} {"CUSTO":>9}')
line(40)
for operation in sale:
    product, quantity = operation
    price = stock[product][1]
    cost = price * quantity
    print(f'{product:<15} {quantity:>4}  x {price:>5.2f}  = {cost:>6.2f}')
    stock[product][0] -= quantity
    total += cost
line(40)
print(f'{"CUSTO TOTAL":^30} = {total:>6.2f}')
line(40)

print('\n')
counter = 0
line(40)
print('ESTOQUE ATUAL' .center(40))
line(40)
for key, data in stock.items():
    counter += 1
    print(f'{"Descrição":<20} {key}')
    print(f'{"Quantidade":<20} {data[0]}')
    print(f'{"Preço":<20} {data[1]:.2f}')
    if counter != endList:
        print()
line(40)
