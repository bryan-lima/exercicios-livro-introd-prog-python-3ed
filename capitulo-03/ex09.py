# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário
# Calcule o total em segundos

days = int(input('Dias: '))
hours = int(input('Horas: '))
minutes = int(input('Minutos: '))
seconds = int(input('Segundos: '))
totalInSeconds = days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds

print(f'\nConvertido em segundos é igual a {totalInSeconds} segundos')
