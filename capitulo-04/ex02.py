# Escreva um programa que pergunte a velocidade do carro de um usuário
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h

velocity = int(input('Qual é a velocidade atual do carro? '))

if velocity > 80:
    print(f'Você foi multado em R$ {(velocity - 80) * 5:.2f}!')
if velocity <= 80:
    print('Sua velocidade está OK.')
