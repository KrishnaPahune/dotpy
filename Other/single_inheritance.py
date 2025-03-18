class Animal:
    def __init__(self,name,species):
       self.n = name
       self.s = species

    def make_sound(self):
        print("Animal makes a sound")


class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name,species="cat")
        self.b = breed
    def make_sound(self):
        print(f"The {self.n} {self.s} Meows!")



c = Cat("persian","persian")
c.make_sound()
print(c.s)
print(c.b)