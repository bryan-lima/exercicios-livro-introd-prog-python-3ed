# O que acontece quando a lista já está ordenada?
# Rastreie o Programa 6.20, mas com a lista L = [1, 2, 3, 4, 5]

# → Resposta: O programa passará pelo segundo while, sem realizar qualquer alteração,
# e finalizará logo em seguida, quando entrar em "for not change", exibindo os valores da lista logo após

L = [1, 2, 3, 4, 5]
end = 5

while end > 1:
    changed = False
    x = 0
    while x < end - 1:
        if L[x] > L[x + 1]:
            changed = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not changed:
        break
    end -= 1

for e in L:
    print(e)

