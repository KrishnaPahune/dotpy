'''Display absolute value, square root and cube root of a number'''
import math
def number(a):
    absolute_value=abs(a)
    square_root=math.sqrt(abs(a))
    cube_root=math.cbrt(abs(a))
    return absolute_value,square_root,cube_root

a=int(input("Enter a number: "))
absolute_value,square_root,cube_root=number(a)
print(f"Absolute value of {a} is {absolute_value}")
print(f"The square root of {a} is: {square_root}")
print(f"The cube root of {a} is: {cube_root}")
