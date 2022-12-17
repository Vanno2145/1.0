#Первый класс: 4 атрибута класса, 5 атрибутов обьекта
class Cat:
    tails = 1
    ears = 2
    eyes = 2
    paws = 4
    print("___cat___")
    def __init__(self):
        self.name = "Tobi"
        self.age = 5
        self.height = 30
        self.color = "Black"
        self.coloreyes = "Green"

st1 = Cat()
print(st1.color)
print(st1.age)
print(st1.coloreyes)
print(st1.name)
print(st1.height)

#Второй класс: 3 атрибута класса, 5 атрибутов обьекта

class Cars:
    wheels = 4
    lights = 4
    wipers = 4
    print("___car___")
    def __init__(self):
        self.extraweel = "No"
        self.color = "Yellow"
        self.clas = "Supercar"
        self.maxspeed = "280"
        self.price = "5 millions"

c1 = Cars()
print(c1.clas)
print(c1.color)
print(c1.maxspeed)
print(c1.price)
print(c1.extraweel)
