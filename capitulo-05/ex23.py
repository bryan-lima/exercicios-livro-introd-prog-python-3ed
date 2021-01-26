# Escreva um programa que leia um número verifique se é ou não um número primo
# Para fazer ess verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido
# Se o resto de uma dessas divisões for igual a zero, o número não é primo
# Observe que 0 e 1 não são primos e que o 2 é o único número primo que é par

n = int(input('\nDigite um número inteiro: '))

if n < 0:
    print('Opção inválida! Permitido apenas números positivos.')

if n == 0 or n == 1:
    print(f'{n} Não é número primo! 0 e 1 são casos especiais.')
else:
    if n == 2:
        print(f'{n} é um número primo! É o único número par que é primo.')
    elif n % 2 == 0:
        print(f'{n} não é número primo! Qualquer número par além de 2, não é primo.')
    else:
        counter = 3
        while counter < n:
            if n % counter == 0:
                break
            counter += 2
        if counter == n:
            print(f'{n} é um número primo!')
        else:
            print(f'{n} não é número primo!')
