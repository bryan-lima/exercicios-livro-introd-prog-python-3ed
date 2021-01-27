# Escreva um programa que leia três strings
# Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira
# 1ª string: AATTCGAA
# 2ª string: TG
# 3ª string: AC
# Resultado: AAAACCAA

str1 = str(input('\nDigite a primeira string: '))
str2 = str(input('Digite a segunda string: '))
str3 = str(input('Digite a terceira string: '))

if len(str2) == len(str3):
    result = ''
    for letra in str1:
        position = str2.find(letra)
        if position != -1:
            result += str3[position]
        else:
            result += letra

    if result == '':
        print('\nTodos os caracteres foram removidos.')
    else:
        print(f'\nOs caracteres {str2} foram substituídos por {str3} em {str1}, gerando: {result}')
else:
    print('\nERRO: A segunda e a terceira string devem ter o mesmo tamanho.')
