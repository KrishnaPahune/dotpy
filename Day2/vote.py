age = int(input("Enter your age: "))
nationality = bool(input("Are you Indian? "))

if (nationality=="yes"):
    print("You are Indian")
    if(age>18):
        print("You are elligible to vote.")
    else:
        print("you are not elligible to vote since you are not 18+")
else:
    print("you are not elligible to vote since you are not Indian")