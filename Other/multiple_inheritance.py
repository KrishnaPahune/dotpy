class Employee:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"The name of employee is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance
    
    def show(self):
        print(f"The dance is {self.dance}")
    
class dancerEmployee(Dancer,Employee):
    def __init__(self,name,dance):
        Employee.__init__(self,name)
        Dancer.__init__(self,dance)

o = dancerEmployee("Krishna","bhangda")
o.show()
print(dancerEmployee.mro()) #Shows the order for finding the methods