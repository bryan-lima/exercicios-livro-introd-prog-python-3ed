# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis:
# matéria1, matéria2 e matéria3

# matter1 > 7 and matter2 > 7 and matter3 > 7

matter1 = float(input('\nDigite a nota da primeira matéria: '))
matter2 = float(input('Digite a nota da segunda matéria: '))
matter3 = float(input('Digite a nota da terceira matéria: '))

if matter1 > 7 and matter2 > 7 and matter3 > 7:
    print('\nAprovado!')
else:
    print('\nReprovado!')
