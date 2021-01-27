# Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira
# 1ª string: AATTGGAA
# 2ª string: TG
# 3ª string: AAAA

# str1 = 'AATTGGAA'
# str2 = 'TG'
#
# print(f'\nPrimeira string: {str1}')
# print(f'Segunda string: {str2}')

str1 = str(input('\nPrimeira string: '))
str2 = str(input('Segunda string: '))

str3 = ''

for letter in str1:
    if letter not in str2:
        str3 += letter

if str3 == '':
        print('Todos os caracteres foram removidos.')
else:
    print(f'\nCaracteres {str2} removidos de {str1}, sobrando apenas: {str3}')
