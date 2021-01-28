# Usando a função mdc definida no exercício anterior, defina uma função para calcular o menor múltiplo comum (M.M.C) entre dois números

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    return abs(a*b) / mdc(a, b)


print(f"MMC 10 e 5 -->  {mmc(10, 5)}")
print(f"MMC 32 e 24 --> {mmc(32, 24)}")
print(f"MMC 5 e 3 -->   {mmc(5, 3)}")
