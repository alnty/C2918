class Student:
    def __init__(self, name="Student"):
        self.name = name
class Schooldiary:
    def __init__(self, diary):
        self.algebra = 0
        self.geometry = 0
        self.geography = 0
        self.english = 0
        self.biology = 0
    def make_algebra(self):
        self.algebra +=  1
    def make_geometry(self):
        self.geometry +=  1
    def make_geography(self):
        self.geography +=  1
    def make_english(self):
        self.english +=  1
    def make_biology(self):
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