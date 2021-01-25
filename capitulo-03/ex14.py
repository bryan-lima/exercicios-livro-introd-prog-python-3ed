# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

def line(size):
    print('-' * size)


line(40)
print('ALUGUEL DE CARROS' .center(40))
line(40)
kmRun = int(input('KM rodados: '))
rentedDays = int(input('Quantidade de dias alugados: '))

valuePerKm = 0.15
dailyRentalPrice = 60

valuePayable = kmRun * valuePerKm + rentedDays * dailyRentalPrice
line(40)
print(f'O valor a pagar é de R$ {valuePayable:.2f}' .center(40))
line(40)
