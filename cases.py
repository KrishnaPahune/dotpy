x = "Y"
while(x == "Y"):
  print("What are you looking for?... \n1. Your Name \n2. Your Age \n3. Your Address \n4. Your Phone Number \n5. Your Email Address")
  choice = int(input("Enter your choice: "))
  match choice:
    case 1:
      print("Your name is Kris")
      x = input(("Do you want to continue?[Y/N] "))
      
    case 2:
      print("Your age is infinite")
      x = input(("Do you want to continue?[Y/N] "))

    case 3:
      print("Your address is in the dark")
      x = input(("Do you want to continue?[Y/N] "))

    case 4:
      print("Your phone number is 000-000-0000")
      x = input(("Do you want to continue?[Y/N] "))

    case 5:
      print("Your email address is oqibz@example.com")
      x = input(("Do you want to continue?[Y/N] "))

    case _ if choice == -7:
      print("Entering the dark realms...")
      x = input(("Do you want to continue?[Y/N] "))

    case _ if choice == 132:
      print("The Heavens are yours")
      x = input(("Do you want to continue?[Y/N] "))

    case _:
      print("Traitor Detected")
      x = input(("Do you want to continue?[Y/N] "))

