class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)
    
    def area(self):
        print(f"Area is {3.14 * super().area()}")

circle = Circle(10)
circle.area()