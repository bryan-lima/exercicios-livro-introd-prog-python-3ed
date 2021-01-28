# Escreva um generator capaz de gerar a série dos números primos

def generator_prime_numbers(n):
    position = 1
    yield 2
    divider = 3
    dividend = 3

    while position < n:
        if dividend % divider == 0:
            if dividend == divider:
                yield dividend
                position += 1
            dividend += 2
            divider = 3
        elif divider < dividend:
            divider += 2
        else:
            dividend += 2


for x in generator_prime_numbers(20):
    print(x)
