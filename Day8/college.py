class college:
    def fun1(self,name,address):
        print("Name of the college is: ",name)
        print("Address of college: ",address)
    
    def fun2(self):
        self.college_id=123
        self.department="I.T"
        print("College id: ",self.college_id)
        print("Department: ",self.department)

obj1=college()
obj1.fun1("PREC","Loni")
obj1.fun2()