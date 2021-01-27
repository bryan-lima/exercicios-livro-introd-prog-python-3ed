# Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja o número desse
# caractere encontrado em uma frase lida
# Exemplo: O rato -> {'O': 1, 'r': 1, 'a': 1, 't': 1, 'o': 1}

phrase = str(input('Digite uma frase: ')).strip()
phrase = ''.join(phrase.split())
phraseDict = {}
for letter in phrase:
    if letter in phraseDict:
        phraseDict[letter] += 1
    else:
        phraseDict[letter] = 1

print(phraseDict)
