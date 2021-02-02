# Faça um programa para listar todos os preços do banco preços.db

import sqlite3
from contextlib import closing
from time import sleep

with sqlite3.connect('prices.db') as connection:
    with closing(connection.cursor()) as cursor:
        print('\n\nListando dados da tabela...')
        sleep(1)
        try:
            cursor.execute('select * from prices')
            while True:
                query = cursor.fetchone()
                if query is None:
                    break
                print(f'\nPRODUTO: {query[0]}\n{"PREÇO:":<8} R$ {query[1]}')
        except Exception as error:
            print(f'\nNão foi possível listar os dados da tabela PRICES\nErro: {error.args}')
        else:
            print(f'\nDados listados com sucesso!')
