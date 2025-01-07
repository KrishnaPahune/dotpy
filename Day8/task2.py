'''Write a python program to demonstrate multiple inheritance where:
1.the class flyable has a method can_fly that prints this object can fly
2.A class bird has a method has_feathers that prints this bird has feathers
3.A class Sparrow inherits from both fliable and bird and adds a method chirp() That Prints Sparrow says chirp chirp
4.Create an object of the sparrow class and call all the methods from its parent and its own method'''

class Flyable:
    def can_fly(self):
        print("This object can fly")
class Bird():
    def has_feathers(self):
        print("This bird has feathers")
class Sparrow(Flyable,Bird):
    def chirp(self):
        print("Sparrow says chirp chirp!")
obj=Sparrow()
obj.can_fly()
obj.has_feathers()
obj.chirp()

