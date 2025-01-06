'''Display a greeting message'''
import time
def greet(hours,name):
    if hours >= 12 and hours <17:
        print(f"Good Afternoon {name}!")
    elif hours >=0 and hours <12:
        print(f"Good Morning {name}!")
    elif hours >=17 and hours < 20:
        print(f"Good Evening {name}!")
    else:
        print(f"Good Night {name}!")

q=input("type yes if you want to enter the time manually or type no if you want to use the current time: ")

if q == "yes":
    hours=int(input("Enter the current hour: "))

else:

    current_time=time.strftime('%H:%M:%S')
    print(f"Current time is: {current_time}")
    hours=int(time.strftime('%H'))
    print("current hour:",hours)
    minutes=int(time.strftime('%M'))
    print("current minute:",minutes)
    seconds=int(time.strftime('%S'))
    print("current second:",seconds)

greet(hours,"Krishna")



    