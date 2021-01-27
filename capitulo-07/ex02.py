# Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas
# 1ª string: AAACTBF
# 2ª string: CBT
# Resultado: CBT
# A ordem dos caracteres gerada não é importante, mas deve conter todas as letras comuns a ambas

# str1 = 'AAACTBF'
# str2 = 'CBT'
#
# print(f'\nPrimeira string: {str1}')
# print(f'Segunda string: {str2}')

str1 = str(input('\nPrimeira string: '))
str2 = str(input('Segunda string: '))

str3 = ''

for letter in str1:
    if letter in str2 and letter not in str3:
        str3 += letter

if str3 == '':
    print(f'\nNenhum caractere de {str2} encontrado em {str1}')
else:
    print(f'\nCaracteres de {str2} encontrado em {str1}: {str3}')
