# Modifique o programa para trabalhar com duas filas
# Para facilitar seu trabalho, considere o comando A para atendimento da fila 1; e B, para atendimento da fila 2
# O mesmo para a chegada de clientes: F para fila 1; e G, para fila 2

def line(size):
    print('-' * size)


last = 10
queue1 = list(range(1, last + 1))
queue2 = list(range(1, last + 1))

while True:
    print()
    line(70)
    print(f'Existem {len(queue1)} clientes na FILA 1')
    print(f'Fila atual: {queue1}')
    line(70)
    print(f'Existem {len(queue2)} clientes na FILA 2')
    print(f'Fila atual: {queue2}')
    line(70)
    print('\nAdicionar cliente na fila:')
    print(' - Digite F para adicionar na fila 1, e G para adicionar na fila 2')
    print('Atendimento:')
    print(' - Digite A para atender da fila 1, e B para atender da fila 2')
    print('Sair do programa:')
    print(' - Digite S')
    operation = str(input('\nOperação (F, G, A, B ou S): ')).strip().upper()

    counter = 0
    leave = False
    while counter < len(operation):
        if operation[counter] == 'A':
            if len(queue1) > 0:
                attended = queue1.pop(0)
                print(f'\nCliente {attended} da FILA 1 atendido')
            else:
                print(f'Fila 1 vazia! Ninguém para atender.')
        elif operation[counter] == 'B':
            if len(queue2) > 0:
                attended = queue2.pop(0)
                print(f'\nCliente {attended} da FILA 2 atendido.')
            else:
                print(f'Fila 2 vazia! Ninguém para atender.')
        elif operation[counter] == 'F':
            last = len(queue1) + 1
            queue1.append(last)
            print('\nChegou um cliente ao final da fila 1.')
            print(f'Existem {len(queue1)} clientes na fila 1.')
            print(f'Fila atual: {queue1}')
        elif operation[counter] == 'G':
            last = len(queue2) + 1
            queue2.append(last)
            print('\nChegou um cliente ao final da fila 2.')
            print(f'Existem {len(queue2)} clientes na fila 2.')
            print(f'Fila atual: {queue2}')
        elif operation[counter] == 'S':
            leave = True
            break
        else:
            print('\nOperação inválida! Digite apenas F, A ou S!')
        counter += 1

    if leave:
        break

print('\nFim da execução!')
