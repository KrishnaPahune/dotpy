#In this code we have implemented operater overloading
#We have given the'+' operator specific implementation using '__add__' method
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
v1 = Vector(1,2,3)
print(v1)

v2 = Vector(4,5,6)
print(v2)

print(v1 + v2)