# Faça um programa que crie o banco de dados preços.db com a tabela preços para armazenar uma lista de preços de venda de produtos
# A tabela deve conter o nome do produto e seu respectivo preço
# O programa também deve inserir alguns dados para teste

import sqlite3
from contextlib import closing
from time import sleep

with sqlite3.connect('prices.db') as connection:
    with closing(connection.cursor()) as cursor:
        print('\n\nCriando tabela...')
        sleep(1)
        try:
            cursor.execute('create table prices(product text, price numeric)')
        except Exception as error:
            print(f'\nNão foi possível criar a tabela PRICES em "prices.db".\nErro: {error.args}')
        else:
            print(f'\nTabela PRICES com os campos PRODUCT (text) e PRICE (real), criados com sucesso em "prices.db"')

        print('\n\nAdicionando dados à tabela...')
        sleep(1)
        products = [('Arroz', '15.78'), ('Feijão', '4.50'), ('Açúcar', '3.20'), ('Queijo', '7.35'),
                    ('Danone', '5.69'), ('Macarrão', '8.99'), ('Suco', '12.90'), ('Pão de forma', '7.75'),
                    ('Mortadela', '16.49'), ('Presunto', '15.92')]
        try:
            cursor.executemany('insert into prices(product, price) values (?, ?)', products)
        except Exception as error:
            print(f'\nNão foi possível adicionar dados à tabela PRICES em "prices.db"\nErro: {error.args}')
        else:
            print('\nDados adicionados à tabela PRICES com sucesso!')

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
