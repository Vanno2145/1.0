import random


class Human:
    def __init__(self, name = 'Human', job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if car.drive():
            pass
        else:
            self.to_repair()
            return
            self.job = Job(Job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness += self.job.gladness
        self.satiety -= 5
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel...')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought food...')
            self.money -= 20
            self.home.food += 20
        elif manage == 'delicacies':
            print('Happy...')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15


    def chill(self):
        self.gladness += 15
        self.home.mess += 5

    def clean_home(self):
        self.home.mess = 0
        self.gladness -= 5

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def date_indexes(self, day):
        day = f'Today the {day} of {self.name} life'
        print(f'{day:=^50}', "\n")
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:^50}', "\n")
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexes = 'Home indexes'
        print (f'{home_indexes: =^50}', "\n")
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        car_indexes = f'{self.car.brand} car indexes'
        print(f'{car_indexes:^50}', "\n")
        print(f'Fuel - {self.car.fuel}')
        print(f'Strength - {self.car.strength}')
    def is_alive(self):
        pass
    def live(self):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print('The car cannot move')
            return False

class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['job_gladness']





job_list = {'C++': {'selary': 70, 'job_gladness': 5},
            'Python': {'selary': 50, 'job_gladness': 10},
            'Java': {'selary': 60, 'job_gladness': 8},
            'PHP': {'selary': 40, 'job_gladness': 7},}

brands_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
                 'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
                 'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
                 'Renault': {'fuel': 80, 'strength': 120, 'consumption': 7}}

car = Auto(brands_of_car)