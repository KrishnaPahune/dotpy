n=50
number_of_guesses = 1

while number_of_guesses <= 5:
    guess=int(input("Guess the correct number: "))

    if guess > n:
        print("Your number is greater than actual number")
    elif guess < n:
        print("your number is smaller than actual number")
    else:
        print("You Guessed the correct number!!!")
        print(f"you guessed correctly in {number_of_guesses} guess")
        break

    remaining_guesses = 5 - number_of_guesses
    number_of_guesses += 1
    print(f"You have {remaining_guesses} remaining guesses")
    print("Try again")
if number_of_guesses > 5:
    print("your guesses are over.\nBetter Luck next time")
