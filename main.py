#Первый класс: 4 атрибута класса, 5 атрибутов обьекта
class Cat:
    tails = 1
    ears = 2
    eyes = 2
    paws = 4
    def __init__(self):
        self.name = "Tobi"
        self.age = 5
        self.height = 30
        self.color = "Black"
        self.coloreyes = "Green"

st1 = Cat()

#Второй класс: 3 атрибута класса, 5 атрибутов обьекта

class Cars:
    wheels = 4
    lights = 4
    wipers = 4
    def __init__(self):
        self.extraweel = "No"
        self.color = "Yellow"
        self.clas = "Supercar"
        self.maxspeed = "280"
        self.price = "5 millions"

c1 = Car()
