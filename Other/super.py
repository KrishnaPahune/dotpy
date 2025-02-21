class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def parent_method(self):
        print("This is a parent Method")

class Programmer(Employee):
    def __init__(self,name,id,lang):
        self.lang=lang
        super().__init__(name,id)
    
    def child_method(self):
        super().parent_method()
        print("This is a child method")

emp = Programmer("harry",450,"python")
print(emp.name)
print(emp.lang)
emp.child_method()


        