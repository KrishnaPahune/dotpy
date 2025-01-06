'''withdraw an amount and display the balance'''
def transaction(process,balance):
    if process=="d":
        amount=int(input("Enter the amount to deposit: "))
        print("Money Deposited")
        balance=balance+amount
    else:
        amount=int(input("Enter the amount to withdraw: "))
        print("Money Withdrawed")
        balance=balance-amount
    return balance

balance=int(input("Enter your balance: "))
print("your current account balance is: ",balance)

while True:
    q=input("Are you performing a transaction? (type yes to perform) ")
    if q=="yes":
        process=input("Deposit or Withdrawal (d/w): ")
    else:
        break
    balance=transaction(process,balance)
    print("Your new balance is: ",balance)
        