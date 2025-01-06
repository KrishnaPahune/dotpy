'''Swapping'''

def swap(a,b):
    print(f"Your numbers are: {a,b}")
    temp=a
    a=b
    b=temp
    return f"{a,b}"
a,b=input("Enter the numbers to swap: ").split()
print(f"Your numbers after swapping are: {swap(a,b)}")

def swapp(a,b):
    print(f"Your numbers are: {a,b}")
    a,b=b,a
    return f"{a,b}"
a,b=input("Enter the numbers to swap: ").split()
print(f"Your numbers after swapping are: {swapp(a,b)}")
