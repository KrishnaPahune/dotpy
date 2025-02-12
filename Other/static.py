class Math:
    def __init__(self,n):
        self.n=n
    
    def addNum(self,num):
        self.n += num
        
    
    @staticmethod
    def add(a,b):
        print(a+b)
a = Math(5)
print(a.n)
a.addNum(5)
print(a.n)
a.add(9,1)
Math.add(9,1)