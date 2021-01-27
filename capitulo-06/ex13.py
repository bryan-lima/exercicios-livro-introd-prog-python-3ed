# A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4]
# Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média

T = [-10, -8, 0, 1, 2, 5, -2, -4]

maximum = minimum = T[0]
summation = 0

for t in T:
    summation += t
    if t < minimum:
        minimum = t
    if t > maximum:
        maximum = t

print(f'\nA cidade de Bons (Bélgica) registrou as últimas temperaturas: {T}')
print(f'A menor temperatura registrada foi {minimum} ºC')
print(f'A maior temperatura registrada foi {maximum} ºC')
print(f'A temperatura média foi {summation / len(T):.0f} ºC')
