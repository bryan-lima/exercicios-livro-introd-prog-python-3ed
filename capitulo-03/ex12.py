# Escreva um programa que calcule o tempo de uma viagem de carro
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem

distance = float(input('Informe a distância a percorrer em km: '))
velocity = int(input('Informe a velocidade média em km/h: '))

time = distance / velocity

# print(f'\nO tempo estimado é de {time:.2f} horas')

time_s = int(time * 3600)  # Conversão de horas para segundos
hours = int(time_s / 3600)  # Parte inteira
time_s = int(time_s % 3600)  # O resto
minutes = int(time_s / 60)
seconds = int(time_s % 60)
print(f'\nO tempo estimado é de {hours:02}:{minutes:02}:{seconds:02}')
