def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
n=int(input())
k=1
while k<=n:
    print(fibonacci(k))
    k += 1





    

