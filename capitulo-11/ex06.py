# Escreva um programa que pergunte o nome do produto e um novo preço
# Usando o banco preços.db, atualize o preço desse produto no banco de dados

import sqlite3
from contextlib import closing

with sqlite3.connect('prices.db') as connection:
    with closing(connection.cursor()) as cursor:
        product = input('\nDigite o produto que deseja atualizar o valor: ')
        cursor.execute('SELECT * FROM prices WHERE product = ?', (product,))
        query = cursor.fetchone()
        if query:
            print('Produto: {0:20s} Preço: R$ {1:6.2f}'.format(*query))
            newPrice = input('Novo preço: R$ ')
            cursor.execute('UPDATE prices SET price = ? WHERE product = ?', (newPrice, product))
            print(f'\nPreço atualizado.')
        else:
            print('\nProduto não encontrado!')
