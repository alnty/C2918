import random
class Kitten:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.thirst = 0
        self.fatigue = 0
        self.gladness = 0
        self.alive = True
    def eat(self):
        print('Time to eat!')
        self.hunger -= 1
        self.gladness += 3
        self.fatigue -= 0.15
    def drink(self):
        print('Time for a water!')
        self.thirst -= 1
        self.gladness += 1
        self.fatigue -= 0.10
    def sleep(self):
        print('Time to sleep!')
        self.hunger += 2
        self.thirst += 1
        self.fatigue -= 3
    def play(self):
        print('Time to play!')
        self.hunger += 3
        self.thirst += 2
        self.fatigue += 3
        self.gladness += 3
    def is_alive(self):
        if self.hunger >= 10:
            print('It turned out sad...')
            self.alive = False
        elif self.thirst >= 10:
            print('It turned out sad...')
            self.alive = False
        elif self.gladness <= 0:
            print('Now your cat is offended.')
            self.alive = False
        elif self.fatigue >= 10:
            print('Cats actually need to sleep 22 hours a day.')
            self.alive = False
    def end_of_day(self):
        print(f'Hunger {self.hunger}')
        print(f'Thirst = {self.thirst}')
        print(f'Fatigue = {self.fatigue}')
        print(f'Gladness = {self.gladness}')
    def live(self, year):
        year = 'Year ' + str(year) + ' of ' + self.name + ' life.'
        print(f'{year:=^50}')
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.eat()
        elif live_cube == 2:
            self.drink()
        elif live_cube == 3:
            self.sleep()
        elif live_cube == 4:
            self.play()
        self.end_of_day()
        self.is_alive()

cat = Kitten(name = "Cat's ")
for year in range(15):
    if cat.alive == False:
        break
    cat.live(year)