'''Leap Year'''
def leap(year):
    if year%4==0:
        print("Leap Year")
    else:
        print("Not a leap a year")
year=int(input("Enter a year: "))
leap(year)