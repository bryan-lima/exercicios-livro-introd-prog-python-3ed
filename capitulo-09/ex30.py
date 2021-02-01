# Modifique o Programa 9.8 para gerar uma lista html, usando os elementos ul e li
# Todos os elementos da lista devem estar dentro do elemento ul, e cada item dentro de um elemento li
# Exemplo:
# <ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>V

moviesDict = {
    'drama': ['Cidadão Kane', 'O Poderoso Chefão'],
    'comédia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora!Tora!Tora!']
}

with open('filmes.html', 'w', encoding='utf-8') as page:
    page.write('''
<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset="utf-8">
        <title>Filmes</title>
    </head>
    <body>
''')
    for genre, movies in moviesDict.items():
        page.write(f'<h1>{genre.capitalize()}</h1>')
        page.write('<ul>')
        for movie in movies:
            page.write(f'<li>{movie}</li>')
        page.write('</ul>')
    page.write('''
    </body>
</html>
''')
