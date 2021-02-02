# Crie classes para representar estados e cidades
# Cada estado tem um nome, sigla e cidades
# Cada cidade tem nome e população
# Escreva um programa de testes que crie três estados com algumas cidades em cada um
# Exiba a população de cada estado como a soma da população de suas cidades

# Solução inicial
#
# class State:
#     def __init__(self, name, uf, citys):
#         self.name = name
#         self.uf = uf
#         self.citys = citys
#
#     def population(self):
#         population = 0
#         for city in self.citys:
#             population += city.population
#         print(f'População total de {self.uf}: {population} habitantes')
#
#
# class City:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#
# jacarei = City('Jacareí', 235416)
# sjcampos = City('São José dos Campos', 729737)
# taubate = City('Taubaté', 317915)
# sp = State('São Paulo', 'SP', [jacarei, sjcampos, taubate])
#
# uberlandia = City('Uberlândia', 699097)
# juiz = City('Juiz de Fora', 573285)
# couto = City('Couto Magalhães de Minas', 4423)
# mg = State('Minas Gerais', 'MG', [uberlandia, juiz, couto])
#
# pelotas = City('Pelotas', 343132)
# stamaria = City('Santa Maria', 283677)
# caxias = City('Caxias do Sul', 517451)
# rs = State('Rio Grande do Sul', 'RS', [pelotas, stamaria, caxias])
#
# print(sp.population())
# print(mg.population())
# print(rs.population())

class State:
    def __init__(self, name, uf):
        self.name = name
        self.uf = uf
        self.citys = []

    def add_city(self, city):
        city.state = self
        self.citys.append(city)

    def population(self):
        return sum([c.population for c in self.citys])


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.state = None

    def __str__(self):
        return f'Cidade (nome={self.name}, população={self.population}, estado={self.state})'


sp = State('São Paulo', 'SP')
sp.add_city(City('Jacareí', 235416))
sp.add_city(City('São José dos Campos', 729737))
sp.add_city(City('Taubaté', 317915))

mg = State('Minas Gerais', 'MG')
mg.add_city(City('Uberlândia', 699097))
mg.add_city(City('Juiz de Fora', 573285))
mg.add_city(City('Couto Magalhães de Minas', 4423))

rs = State('Rio Grande do Sul', 'RS')
rs.add_city(City('Pelotas', 343132))
rs.add_city(City('Santa Maria', 283677))
rs.add_city(City('Caxias do Sul', 517451))

for state in [sp, mg, rs]:
    print(f'Estado: {state.name:<32} Sigla: {state.uf}')
    for city in state.citys:
        print(f'Cidade: {city.name:<32} População: {city.population}')
    print(f'População do Estado: {state.population()}\n')
