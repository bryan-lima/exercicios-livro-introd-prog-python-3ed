# Faça um programa que calcule o aumento de um salário
# Ele deve solicitar o valor do salário e a porcentagem do aumento
# Exiba o valor do aumento e do novo salário

currentSalary = float(input('\nInforme o salário atual: R$ '))
percentageIncrease = float(input('Informe a porcentagem de aumento: '))

increase = currentSalary * percentageIncrease / 100
newSalary = currentSalary + increase

print(f'\nO salário atual é de R$ {currentSalary:.2f}')
print(f'Um aumento de {percentageIncrease}%, representa um aumento de R$ {increase:.2f}')
print(f'Portanto, o valor do salário passa a ser de R$ {newSalary:.2f}')
