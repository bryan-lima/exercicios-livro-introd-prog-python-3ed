# Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias (objetos), especificando o valor de min e max por nome

class Television:
    def __init__(self, min=2, max=14):
        self.switched_on = False
        self.channel = min
        self.cmin = min
        self.cmax = max

    def decrease_channel(self):
        if self.channel - 1 >= self.cmin:
            self.channel -= 1
        else:
            self.channel = self.cmax

    def increase_channel(self):
        if self.channel + 1 <= self.cmax:
            self.channel += 1
        else:
            self.channel = self.cmin


tv1 = Television(min=12, max=89)
tv1.decrease_channel()
print(tv1.channel)
tv1.increase_channel()
print(tv1.channel)

tv2 = Television(min=3, max=125)
tv2.decrease_channel()
print(tv2.channel)
tv2.increase_channel()
print(tv2.channel)
