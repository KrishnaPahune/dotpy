'''Write a program to print average of arguements'''
def avg(*args):
    print(f"The average of arguemennts is: {sum(args)/len(args)}")
avg(10,20,30)

def avg2(args):
    if len(args)==0:
        print("The average of numbers is zero")
    else:
        print(f"The average of numbers is {sum(args)/len(args)}")

numbers=[]
while True:
    n=input("Enter a number or enter done if finish")
    if(n=="done"):
        break
    else:
        numbers.append(int(n))

avg2(numbers)

