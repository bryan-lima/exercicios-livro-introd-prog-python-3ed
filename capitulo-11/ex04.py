# Modifique o programa do Exercício 11.3 de forma a perguntar a dois valores e listar todos os produtos com preços entres esses dois valores

import sys
import sqlite3
from contextlib import closing

with sqlite3.connect('prices.db') as connection:
    with closing(connection.cursor()) as cursor:
        while True:
            price1 = input('\nDigite o menor preço a listar: ')
            price2 = input('Digite o maior preço a listar: ')
            cursor.execute('SELECT * FROM prices WHERE price >= ? AND price <= ?', (price1, price2))
            counter = 0
            while True:
                query = cursor.fetchone()
                if query is None:
                    break
                print(f'\nPRODUTO: {query[0]}\n{"PREÇO:":<8} R$ {query[1]:.2f}')
                counter += 1
            print(f'\nEncontrado {counter} produto(s)')
            while True:
                proceed = str(input('\nNova consulta? [S/N]: ')).strip().upper()[0]
                if proceed == 'S':
                    break
                elif proceed == 'N':
                    sys.exit(0)
                print(f'Digite apenas S ou N. Tente novamente.')
