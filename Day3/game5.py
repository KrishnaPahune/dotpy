questions=["Q1 what is the national animal of India?\na. tiger\tb. cheetah\nc. peacock\td. rhino",
           "Q2 Color of Ashok Chakra?\na. red\tb. green\nc. yellow\td. blue",
           "Q3 National anthem of India?\na.sare jana se accha \tb. Jana Gana Mana\nc. Teri Mitti\td. Vande Mataram",
           "Q4 National emblem of India?\na. Red Fort\tb. Taj Mahal\nc. Tricolor\td. Lion Capital of Ashoka"]
correct=["a","d","b","d"]
print("Welcome to KBC".center(100,"-"))
print()
price=5000
i=0
total = 0
while i < len(questions):
    print("".center(100,"-"))
    print("YE SAWAL APKO DEGA",price,"$")
    print()
    print(questions[i])
    option=input("Enter your choice: ")
    match(option):
        case "a" | "b" | "c" | "d":
            if option == correct[i]:
                print("Correct answer!")
                total=total+price
                print("Your total sum is:",total)
                
            else:
                print("Wrong answer!")
                print("you are fined with 1000$")
                total=total-1000
                print("Your total sum is:",total)
            
            price=price*2
            i=i+1
        case _:
            Q=input("Invalid input! Kya aap quit krna chahte hai?(Yes/No) ")
            if Q=="Yes":
                break
            else:
               print("wahi sawal dobara poocha jayega...")

print("".center(100,"-"))
if(total>0):
    print("Congrats! you are taking home",total,"$")
else:
    print("Sorry! Better Luck next time")