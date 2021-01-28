# Escreva uma função que receba uma string e uma lista
# A função deve comparar a string passada com os elementos da lista, também passada como parâmetro
# Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário

def searchStr(string, lst):
    return string in lst


lstStr = ["AB",  "CD", "EF", "FG"]

print(searchStr("AB", lstStr))
print(searchStr("CD", lstStr))
print(searchStr("EF", lstStr))
print(searchStr("FG", lstStr))
print(searchStr("XYZ", lstStr))
