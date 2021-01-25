# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para inferiores ou iguais, de 15%

salary = float(input('Informe o salário atual: R$ '))

increasePercentage = 0.15

if salary > 1250:
    increasePercentage = 0.10

newSalary = salary * increasePercentage

print(f'\nO aumento de salário será de R$ {newSalary:.2f}')
