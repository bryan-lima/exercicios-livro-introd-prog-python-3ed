# Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para baixo, além do mínimo, ela vá para o canal máximo
# Se mudarmos para cima, além do canal máximo, que volte ao canal mínimo
# Exemplo:
# >>> tv = Televisão(2, 10)
# >>> tv.muda_canal_para_baixo()
# >>> tv.canal
# 10
# >>> tv.muda_canal_para_cima()
# >>> tv.canal
# 2

class Television:
    def __init__(self, min, max):
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


tv = Television(5, 12)

tv.decrease_channel()
print(tv.channel)

tv.increase_channel()
print(tv.channel)
