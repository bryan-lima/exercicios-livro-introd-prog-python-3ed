# Escreva uma função que receba uma string com as opções válidas a aceitar (cada opção é uma letra)
# Converta as opções válidas para letras minúsculas
# Utilize input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção é válida
# Em caso de opção inválida, a função deve pedir ao usuário que digite novamente outra opção

def validatesEntry(msg, options):
    options = options.strip().lower()
    while True:
        choice = str(input(f'\n{msg}')).strip().lower()[0]
        if choice in options:
            break
        else:
            print('Opção inválida!')


validatesEntry('Esolha uma opção (a, b, c ou d): ', 'abcd')
