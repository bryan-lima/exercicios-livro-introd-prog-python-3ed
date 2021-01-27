# Faça um programa que leia uma expressão com parênteses
# Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta
# Exemplo:
# (())          OK
# ()()(()())    OK
# ())           Erro
# Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses
# Ao desempilhar, verifique se o topo da pilha é um abre parênteses
# Se a expressão estiver correta, sua pilha estará vazia no final

expression = str(input('\nDigite uma expressão: ')).strip()

counter = 0
stack = []

while counter < len(expression):
    if expression[counter] == '(':
        stack.append('(')
    if expression[counter] == ')':
        if len(stack) > 0:
            top = stack.pop(-1)
        else:
            stack.append(')')
            break
    counter += 1

if len(stack) == 0:
    print('\nExpressão válida!')
else:
    print('\nExpressão inválida! Uso incorreto dos parênteses.')
