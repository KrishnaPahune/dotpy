'''Single inheritance'''
class A:
    def info1():
        print("This is a parent class")
class B(A):
    def info2():
        print("This is a child class")
obj=B()
B.info1()
B.info2()
print("".center(50,"-"))


'''Multi Level Inheritance'''
class A:
    def info1():
        print("This is a parent class")
class B(A):
    def info2():
        print("This is child of A")
class C(B):
    def info3():
        print("This is child of B")    
obj=C()
C.info1()
C.info2()
C.info3()
print("".center(50,"-"))


'''Multiple Inheritance'''
class A:
    def info1(self):
        print("This is parent1")
class B():
    def info2(self):
        print("this is parent2")
class C(A,B):
    def info3(self):
        print("This is child class")
obj=C()
obj.info1()
obj.info2()
obj.info3()
print("".center(50,"-"))

'''Hierarchical inheritance'''
class A:
    def info1(self):
        print("This is parent1")
class B(A):
    def info2(self):
        print("this is child1")
class C(A):
    def info3(self):
        print("This is child2")
obj1=B()
obj1.info1()
obj1.info2()
obj2=C()
obj2.info1()
obj2.info3()
print("".center(50,"-"))

'''Hybrid inheritance'''
class A:
    def info1(self):
        print("This is parent1")
class B(A):
    def info2(self):
        print("this is child1")
class C(A):
    def info3(self):
        print("This is child2")
class D(B,C):
    def info4(self):
        print("This is the hybrid child")
obj1=D()
obj1.info1()
obj1.info2()
obj1.info3()
obj1.info4()
