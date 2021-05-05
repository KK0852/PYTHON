def fibo(n):
    n1=0
    n2=1
    count=0
    if n<=0:
        print("Please, Enter any positive number:")
    elif n==1:
        print(n1)
    else:
        while count<n:
            print(n1)
            nn=n1+n2
            n1=n2
            n2=nn
            count+=1
n=int(input("Enter a num for fibonacci series:"))
fibo(n)