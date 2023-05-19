class Human:
    def __init__(self, name="Student"):
        self.name = name
class Supplies:
    def __int__(self, books=None, pens=None):
        self.books = books
        self.pens = pens
    def get_books(self):
        print("I'm going to take book from the library.")
        self.books += 1
    def get_pens(self):
        print("I'm going to buy new pen in the store.")
        self.pens += 1
    def live(self, week):
        day = str(week) + " week" + " of " + "the " + self.name + "'s" ' life.'
        print(f'{day:=^35}')
        live_cube = random.randint(1, 2)
        if live_cube == 1:
            self.get_books()
        elif live_cube == 2:
            self.get_pens()