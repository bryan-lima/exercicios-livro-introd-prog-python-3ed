# Adicione os atributos tamanho e marca à classe Televisão
# Crie dois objetos Televisão e atribua tamanhos e marcas diferentes
# Depois, imprima o valor desses atributos de forma a confirmar a independência dos valores de cada instância (objeto)

class Television:
    def __init__(self):
        self.switched_on = False
        self.channel = 2
        self.size = 30
        self.brand = 'Samsung'


tv1 = Television()
tv1.size = 32
tv1.brand = 'Sony'

tv2 = Television()
tv2.size = 55
tv2.brand = 'Panasonic'

print(f'TV1 → Tamanho: {tv1.size}  |  Marca: {tv1.brand}')
print(f'TV2 → Tamanho: {tv2.size}  |  Marca: {tv2.brand}')
