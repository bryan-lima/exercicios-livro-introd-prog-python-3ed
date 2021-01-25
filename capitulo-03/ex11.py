# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto
# Exiba o valor do desconto e o preço a pagar

currentPrice = float(input('\nInforme o preço do produto: R$ '))
discountPercentage = float(input('Digite o percentual de desconto: '))

discount = currentPrice * discountPercentage / 100
newPrice = currentPrice - discount

print(f'\nO valor atual do produto é de R$ {currentPrice:.2f}')
print(f'Um desconto de {discountPercentage}%, representa um desconto de R$ {discount:.2f}')
print(f'Com o desconto, o produto passa a custar R$ {newPrice:.2f}')
