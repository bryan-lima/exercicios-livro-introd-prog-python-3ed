# Escreva um programa que realize consultas do banco de dados preços.db, criado no Exercício 11.1
# O programa deve perguntar o nome do produto e listar seu preço

import sqlite3
from contextlib import closing

with sqlite3.connect('prices.db') as connection:
    with closing(connection.cursor()) as cursor:
        while True:
            product = str(input('\nDigite o nome do produto para pesquisar o preço (0 para sair): ')).strip()
            if product == '0':
                break
            cursor.execute('SELECT * FROM prices WHERE product = ?', (product,))
            counter = 0
            while True:
                query = cursor.fetchone()
                if query is None:
                    if counter == 0:
                        print('\nProduto não encontrado!')
                    break
                print(f'\nPRODUTO: {query[0]}\n{"PREÇO:":<8} R$ {query[1]:.2f}')
                counter += 1
