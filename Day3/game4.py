'''Create a program capable of displaying questions to the user like KBC
   Use list data type to store the questions and their correct answers.
   Display the final output the person is taking home after playing the game'''

questions=["what is the national animal of India?","most polluted city?","National anthem of India?","National song of India?"]
ans=["Tiger","Delhi","Jana Gana Mana","Vande Mataram"]
user_ans=[]

print("Welcome to KBC".center(100,"-"))
print()
i=1
k=0
price=5000
total=0
for question in questions:
    print("Q",i,end=" ")
    print(question,end="     ")
    print("Price:",price)
    user=input()
    print()
    if user.lower() == ans[k].lower():
        total = total+price
    k=k+1
    i=i+1
    price=price*2
print()
print("Total:",total)

    





