class Animal:
    def __init__(self,species):
        self.species = species
    
    def show(self):
        print(f"This is a {self.species}")

class Dog(Animal):
    def __init__(self,species,breed):
        super().__init__(species)
        self.breed=breed

    def show(self):
        Animal.show(self)
        print(f"Its breed is {self.breed}")
    
class Puppy(Dog):
    def __init__(self,species,breed,name):
        super().__init__(species,breed)
        self.name=name
    
    def show(self):
        Dog.show(self)
        print(f"its name is {self.name}")

o = Puppy("Dog","Labrodor","Tom")
o.show()