class Animal:
    def __init__(self, name="Animal"):
        self.name = name
class Zoo:
    def __init__(self, species):
        self.species = []
    def add_kind(self, animal):
        self.species.append(animal)
    def print_animal_species(self):
        if self.species != []:
            print(f"Types of animals in Zoo: ")
            for species in self.species:
                print(species.name)
        else:
            print(f"There are no animals.")
cat = Animal("Cat")
dog = Animal("Dog")
lizard = Animal("Lizard")
rabbit = Animal("Rabbit")
hamster = Animal("Hamster")
zoo = Zoo("Zoo")

zoo.add_kind(cat)
zoo.add_kind(dog)
zoo.add_kind(lizard)
zoo.add_kind(rabbit)
zoo.add_kind(hamster)
zoo.print_animal_species()