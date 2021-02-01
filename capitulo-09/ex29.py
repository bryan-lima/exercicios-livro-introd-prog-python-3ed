# Modifique o Programa 9.8 para utilizar o elemento p em vez de h2 nos filmes

# Programa 9.8 do livro, página 210
# Programa 9.8 - Geração de uma página web a partir de um dicionário
#
# filmes = {
#     'drama': ['Cidadão Kane', 'O Poderoso Chefão'],
#     'comédia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
#     'policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
#     'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
# }
#
# with open('filmes.html', 'w', encoding='utf-8') as página:
#     página.write('''
# <!DOCTYPE html>
# <html lang="pt-BR">
# <head>
# <meta charset="utf-8">
# <title>Filmes</title>
# </head>
# <body>
# ''')
#     for c, v in filmes.items():
#         página.write(f'<h1>{c}</h1>\n')
#         for e in v:
#             página.write(f'<h2>{e}</h2>\n')
#     página.write('</body></html>')

moviesList = {
    'drama': ['Cidadão Kane', 'O Poderoso Chefão'],
    'comédia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
}

with open('filmes.html', 'w', encoding='utf-8') as page:
    page.write('''
<!DOCTYPE hmlt>
<html lang="pt-BR">
    <head>
        <meta charset="utf-8">
        <title>Filmes</title>
    </head>
    <body>
''')
    for genre, movies in moviesList.items():
        page.write(f'<h1>{genre}</h1>\n')
        for movie in movies:
            page.write(f'<p>{movie}<p>\n')
    page.write('''
    </body>
</html>''')
