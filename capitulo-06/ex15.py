# O que acontece quando dois valores são iguais?
# Rastreie o Programa 6.20, mas com a lista L = [3, 3, 1, 5, 4]

# → Resposta: Na primeira verificação 3, 3 são considerados como na ordem correta
# No próximo passo, ao verificar o segundo número 3 com 1, ocorre uma troca, ficando assim: [3, 1, 3, 5, 4]
# Quando a verificação reiniciar, o primeiro 3 também será trocado com o número 1, ficando assim: [1, 3, 3, 4, 5]

L = [3, 3, 1, 5, 4]
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
