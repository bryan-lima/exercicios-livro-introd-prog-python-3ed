# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas

distance = int(input('Qual distância irá percorrer? '))

if distance <= 200:
    passage = 0.50 * distance
else:
    passage = 0.45 * distance

print(f'\nO preço da passagem é de R$ {passage:.2f}')
