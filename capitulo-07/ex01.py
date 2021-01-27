# Escreva um programa que leia duas strings
# Verifique se a segunda ocorre dentro da primeira e imprima a posição de início
# 1ª string: AABBEFAATT
# 2ª string: BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT

# str1 = 'AABBEFAATT'
# str2 = 'BE'
#
# print(f'\nPrimeira string: {str1}')
# print(f'Segunda string: {str2}')

str1 = str(input('\nPrimeira string: '))
str2 = str(input('Segunda string: '))

position = str1.find(str2)

if position == -1:
    print(f'\n{str2} não encontrado em {str1}')
else:
    print(f'\n{str2} encontrado na posição {position} de {str1}')
