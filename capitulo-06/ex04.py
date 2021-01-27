# O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?

# → Resposta: Ocorre um erro, e a execução para. IndexError: pop from empty list

# Programa 6.7 do livro, página 107
# Programa 6.7 - Simulação de uma fila de banco

last = 10
queue = list(range(1, last + 1))

while True:
    print(f'\nExistem {len(queue)} clientes na fila')
    print(f'Fila atual: {queue}')
    print(f'\nDigite F para adicionar um cliente ao fim da fila,')
    print(f'ou A para realizar atendimento. S para sair: ')
    operation = input('\nOperação (F, A ou S): ').strip().upper()
    if operation == 'A':
        if len(queue) > 0:
            attended = queue.pop(0)
            print(f'Cliente {attended} atendido')
        else:
            print(f'Fila vazia! Ninguém para atender')
    elif operation == 'F':
        last += 1
        queue.append(last)
    elif operation == 'S':
        break
    else:
        print('Operação inválida! Digite apenas F, A ou S!')
