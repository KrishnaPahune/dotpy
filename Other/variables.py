class Employee:
    companyName="factory"
    noOfEmployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        Employee.noOfEmployee+=1

    def show(self):
        print(f"the raise of {self.name} working in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

emp1=Employee("Krishna")
emp1.show()
emp1.raise_amount=0.5
emp1.show()
emp2 = Employee("harry")
emp2.companyName="Apple"
emp2.show()    