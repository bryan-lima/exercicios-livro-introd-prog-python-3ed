# Reescreva o Programa 8.2 de forma a utilizar for em vez de while

# Programa 8.2 do livro, página 162
# Programa 8.2 - Como não escrever uma função
#
# def soma(L):
#     total = 0
#     x = 0
#     while x < 5:
#         total += L[x]
#         x += 1
#     return total
#
#
# L = [1, 7, 2, 9, 15]
# print(soma(L))
# print(soma([7, 9, 12, 3, 100, 20, 4]))


def summation(lst):
    total = 0
    for number in lst:
        total += number
    return total


L = [1, 7, 2, 9, 15]
print(summation(L))
print(summation([7, 9, 12, 3, 100, 20, 4]))
