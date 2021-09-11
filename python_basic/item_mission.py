class item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def status(self):
        print(self.name)
        print(self.price)
        print(self.weight)
        print(self.isdropable)

class Sword(item):
    pass

