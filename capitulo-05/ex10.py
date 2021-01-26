# Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões

points = 0
question = 1

while question <= 3:
    answer = str(input(f'Resposta da questão {question}: ')).strip()
    if question == 1 and (answer == 'b' or answer == 'B'):
        points += 1
    if question == 2 and (answer == 'a' or answer == 'A'):
        points += 1
    if question == 3 and (answer == 'd' or answer == 'D'):
        points += 1
    question += 1

print(f'\nO aluno fez {points} ponto(s)')
