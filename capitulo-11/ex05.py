# Escreva um programa que aumente o preço de todos os produtos do banco preços.db em 10%

import sqlite3
from contextlib import closing

with sqlite3.connect('prices.db') as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute('UPDATE prices SET price = price * 1.1')
        print(f'\nRegistros alterados: {cursor.rowcount}\n')
        cursor.execute('SELECT * FROM prices')
        for query in cursor.fetchall():
            print('Produto: {0:20s} Preço: {1:6.2f}'.format(*query))
