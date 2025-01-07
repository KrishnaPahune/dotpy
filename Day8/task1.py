'''Write the python program to demonstrate single inheritance where:
1. A parent Class animal has an attribute name and a method display_name To print the Name
2.A child class dog inherits from animal and adds a method bark that prints a message indicating the dog is barking
3.Create an object of the dog class set its name and call both display_name and bark methods'''

class Animal:
    name=""
    def display_name(self):
        print("Name of animal is:",self.name)
class Dog(Animal):
    def bark(self,name):
        print(f"{name} is barking")
obj=Dog()
obj.name="Tommy"
obj.display_name()
obj.bark(obj.name)

