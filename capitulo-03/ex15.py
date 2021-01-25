# Escreva um programa para calcular a redução do tempo de vida de fumante
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá
# Exiba o total em dias

cigarettesPerDay = int(input('\nFuma quantos cigarros por dia? '))
quantityYearsYouSmoke = int(input('Fuma há quantos anos? '))

lifeLostMinutes = quantityYearsYouSmoke * 365 * cigarettesPerDay * 10
lifeLostDays = lifeLostMinutes / (24 * 60)  # Um dia tem 24 horas * 60 minutos

print(f'\nRedução de vida em {lifeLostDays:.0f} dias')
