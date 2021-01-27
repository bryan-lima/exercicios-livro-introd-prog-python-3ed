# Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez
# Atualmente, apenas um comando pode ser inserido por vez
# Altere-o de forma a considerar operação como uma string
# Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa

# Programa 6.7 do livro, página 107
# Programa 6.7 - Simulação de uma fila de banco

last = 10
queue = list(range(1, last + 1))

while True:
    print(f'\nExistem {len(queue)} clientes na fila')
    print(f'Fila atual: {queue}')
    print(f'\nDigite F para adicionar um cliente ao fim da fila,')
    print(f'ou A para realizar atendimento. S para sair: ')
    operation = str(input('\nOperação (F, A ou S): ')).strip().upper()

    counter = 0
    leave = False
    while counter < len(operation):
        if operation[counter] == 'A':
            if len(queue) > 0:
                attended = queue.pop(0)
                print(f'\nCliente {attended} atendido')
            else:
                print(f'Fila vazia! Ninguém para atender')
        elif operation[counter] == 'F':
            last += 1
            queue.append(last)
            print('\nChegou um cliente ao final da fila.')
            print(f'Existem {len(queue)} clientes na fila')
            print(f'Fila atual: {queue}')
        elif operation[counter] == 'S':
            leave = True
            break
        else:
            print('\nOperação inválida! Digite apenas F, A ou S!')
        counter += 1

    if leave:
        break

print('\nFim da execução!')
