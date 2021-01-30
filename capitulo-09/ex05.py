# Crie um programa que inverta a ordem das linhas do arquivo pares.txt
# A primeira linha deve conter o maior número; e a última, o menor

# Solução inicial
#
# pairs = open('pares.txt', 'r')
# pairsReverse = open('pares-invertido.txt', 'w')
#
# contentPairs = pairs.readlines()
# contentPairs.reverse()
#
# for line in contentPairs:
#     pairsReverse.write(line)
#
# pairs.close()
# pairsReverse.close()
#
# print(f'\nOperação finalizada com sucesso!')

try:
    with open('pares.txt', 'r') as pairs, open('pares-invertido.txt', 'w') as pairsReverse:
        contentPairs = pairs.readlines()
        contentPairs.reverse()

        for line in contentPairs:
            pairsReverse.write(line)
except Exception as error:
    print(f'\nOcorreu um erro: {error.args[1]}')
else:
    print(f'\nOperação finalizada com sucesso!')
