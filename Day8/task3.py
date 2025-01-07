'''Write a python program to demonstrate multi level inheritance where
1.a base class vehicle has a method type that prints this is a vehicle
2.a class car inherits from vehicle and adds a method brand(name) to print the brand of the car
3.A class sports car inherits from car and adds a method top speed(speed) to print the top speed of the car
4.Create an object of the sports car call all the methods and demonstrate the hierarchy'''

class vehicle:
    def type(self):
        print("This is a vehicle")
class car(vehicle):
    def brand(self,brand):
        print("the brand of the car is",brand)
class sportsCar(car):
    def topSpeed(self,topSpeed):
        print("The top speed of the car is",topSpeed)
obj=sportsCar()
obj.type()
obj.brand("bharatbenz")
obj.topSpeed(500)
        
