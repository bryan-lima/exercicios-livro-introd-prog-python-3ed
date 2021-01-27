# Modifique o Programa 6.2 para ler 7 notas em vez de 5

# Programa 6.2 do livro, página 99
# Programa 6.2 - Cálculo da média com notas digitadas

notes = [0, 0, 0, 0, 0, 0, 0]
summation = 0
counter = 0

print()
while counter < len(notes):
    notes[counter] = float(input(f'Nota {counter}: '))
    summation += notes[counter]
    counter += 1

counter = 0

print()
while counter < len(notes):
    print(f'Nota {counter}: {notes[counter]:.1f}')
    counter += 1

print(f'\nMédia: {summation / len(notes):.1f}')
