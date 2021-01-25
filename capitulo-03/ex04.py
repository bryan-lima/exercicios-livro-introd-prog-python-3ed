# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto
# Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00

salary = float(input('\nInforme seu salário: '))

if salary > 1200:
    print('\nPrecisa pagar imposto!')
else:
    print('\nNão precisa pagar imposto!')
