# Utilizando o que aprendemos com funções, modifique o construtor da classe Televisão de forma que min e max sejam
# parâmetros opcionais, em que min vale 2 e max vale 14, caso outro valor não seja passado

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


tv = Television()
tv.decrease_channel()
print(tv.channel)
tv.increase_channel()
print(tv.channel)

tv1 = Television()
print(f'Canal atual: {tv1.channel}  | Canal mínimo: {tv1.cmin}  | Canal máximo: {tv1.cmax}')

tv2 = Television(7, 60)
print(f'Canal atual: {tv2.channel}  | Canal mínimo: {tv2.cmin}  | Canal máximo: {tv2.cmax}')
