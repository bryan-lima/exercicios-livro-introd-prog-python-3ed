# Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista, vistos no Capítulo 7

# Programa 8.1 do livro, página 159
# Programa 8.1 - Pesquisa em uma lista
#
# def pesquise(lista, valor):
#     for x, e in enumerate(lista):
#         if e == valor:
#             return x
#     return None
#
#
# L = [10, 20, 25, 30]
# print(pesquise(L, 25))
# print(pesquise(L, 27))


def search(lst, value):
    if value in lst:
        return lst.index(value)
    return None


L = [10, 20, 25, 30]
print(search(L, 25))
print(search(L, 27))
