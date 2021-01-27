# Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas
# 1ª string: CTA
# 2ª string: ABC
# 3ª string: BT
# A ordem dos caracteres da terceira string não é importante

# str1 = 'CTA'
# str2 = 'ABC'
#
# print(f'\nPrimeira string: {str1}')
# print(f'Segunda string: {str2}')

str1 = str(input('\nPrimeira string: '))
str2 = str(input('Segunda string: '))

str3 = ''

for letter in str1:
    if letter not in str2 and letter not in str3:
        str3 += letter

for letter in str2:
    if letter not in str1 and letter not in str3:
        str3 += letter

if str3 == '':
    print('Caracteres incomuns não encontrados.')
else:
    print(f'\nOs caraceteres incomuns entre as duas strings são: {str3}')
