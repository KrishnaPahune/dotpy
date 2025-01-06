'''Arithmetic Non-Parameter'''

def add():
    a=5
    b=6
    c=a+b
    print(c)
add()

'''Arithmetic Parameter'''
def add(i,j):
    print(f"Addition is {i+j}")
add(5,6)

'''Arithmetic Parameter Return'''
def add(i,j):
    c=i+j
    return c
print(add(5,6))

'''Even Odd'''
def even_odd():
    a = int(input("Enter a number: "))
    if(a%2==0):
      print("Even")
    else:
      print("odd")
even_odd()
