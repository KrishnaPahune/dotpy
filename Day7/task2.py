'''To write a function rhat displays a string repetetively'''
def st(n,a):
    i=1
    while i <= n:
        print(a)
        i+=1
    print("ENd")
a=input("Enter a string to be repeated: ")
n=int(input("How much time do you want to repeat? "))
st(n,a)
