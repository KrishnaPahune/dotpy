import random

while True:
    user_action=input("Enter your choice (rock/paper/scissor): ")
    computer_action=random.choice(["rock","paper","scissor"])
    print(f"your choice is {user_action} and computer's choice is {computer_action}")
    if user_action==computer_action:
        print(f"Both choose {user_action}. Its a Tie!")
    
    elif user_action=="rock":
        if computer_action=="paper":
            print("paper covers rock. You Lose!")
        else:
            print("rock kills scissor. You Win!")
    
    elif user_action=="paper":
        if computer_action=="rock":
            print("paper covers rock. You Win!")
        else:
            print("scissor kills paper. You Lose!")
    else:
        if computer_action=="paper":
            print("scissor kills paper. You Win!")
        else:
            print("rock kills scissor. You Lose!")       
    print("-".center(50,"-"))
    play_again=input("do you want to play agin?(yes/no)")
    if play_again.lower()=="no":
        break
