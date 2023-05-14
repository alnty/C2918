import random
class Schooldiary:
    def __init__(self, diary):
        #Тематичні оцінки на початку місяця. Їх можна або покращити, або погіршити.
        self.algebra = 5
        self.geometry = 5
        self.geography = 5
        self.english = 5
        self.biology = 5
    def do_algebra(self):
        self.algebra +=  1
    def do_geometry(self):
        self.geometry +=  1
    def do_geography(self):
        self.geography +=  1
    def do_english(self):
        self.english +=  1
    def do_biology(self):
        self.biology +=  1
    def to_chill(self):
        self.algebra -= 1
        self.geometry -=  1
        self.geography -= 1
        self.english -= 1
        self.biology -= 1
    def to_sleep(self):
        self.algebra -= 1
        self.geometry -= 1
        self.geography -= 1
        self.english -= 1
        self.biology -= 1

    def is_alive(self):
        if self.algebra <= 0:
            print("You don't like fractions?")
        elif self.geometry <= 0:
            print("Are you still laughing at the word «parallelepiped»?")
        elif self.geography <= 0:
            print("So, where is Monaco?")
        elif self.english <= 0:
            print("When we use Present Continuous?")
        elif self.biology <= 0:
            print("Don't tell me you can only talk about one topic...")

    def end_of_day(self):
        print(f"Algebra - {self.algebra}")
        print(f"Geometry - {self.geometry}")
        print(f"Geography - {self.geography}")
        print(f"English - {self.english}")
        print(f"Biology - {self.biology}")

    def live(self, day):
        day = 'Day ' + str(day) + ' of ' + self.name + ' life.'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 8)
        if live_cube == 1:
            self.do_algebra()
        elif live_cube == 2:
            self.do_geometry()
        elif live_cube == 3:
            self.do_geography()
        elif live_cube == 4:
            self.do_english()
        elif live_cube == 5:
            self.do_biology()
        elif live_cube == 6:
            self.to_chill()
        elif live_cube == 7:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()
class Student:
    def __init__(self, name="Student"):
        self.name = name
for day in range(366):
    print(end_of_day)