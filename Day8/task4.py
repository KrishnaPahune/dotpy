'''Write a python program to demonstrate hierarchical inheritance where:
1.the parent class shape has a method identify that prints this is the shape
2.A child class circle inherits from shape and adds a method area(radius) to calculate and print the area of the circle
3.Another child class rectangle inherits from shape and adds a method area(length, width) to calculate and print the area of rectangle
4.Create objects of both circle and rectangle classes and call their respective methods'''

import math
class Shape:
    def identify(self):
        print("This is a shape")
class circle(Shape):
    def area(self,radius):
        area=math.pi*radius**2
        print(f"The radius of the circle is {radius} and its area is {area}")
class rectangle(Shape):
    def area(self,length,width):
        area=length*width
        print(f"The rectangle having length {length} and width {width},has an area of {area}")
obj1=circle()
obj1.identify()
obj1.area(10)
obj2=rectangle()
obj2.identify()
obj2.area(5,6)