# Atualmente, a classe Televisão inicializa o canal com 2
# Modifique a classe Televisão de forma a receber o canal inicial em seu construtor

class Television:
    def __init__(self, channel, min, max):
        self.switched_on = False
        self.channel = channel
        self.cmin = min
        self.cmax = max

    def decrease_channel(self):
        if self.channel - 1 >= self.cmin:
            self.channel -= 1

    def increase_channel(self):
        if self.channel + 1 <= self.cmax:
            self.channel += 1


tv = Television(5, 1, 99)
print(tv.channel)
