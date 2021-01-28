# Escreva uma função para validar uma variável string
# Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres
# Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo, e falso, caso contrário

def validateStr(string, minimum, maximum):
    return minimum <= len(string) <= maximum


s = str(input('Digite uma string: '))
sizes = [[5, 12], [1, 5], [2, 5], [3, 5], [1, 10]]

for index, size in enumerate(sizes):
    print(f'A string "{s}" tem tamanho entre {size[0]} e {size[1]}: {validateStr(s, size[0], size[1])}')
