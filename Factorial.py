def fac(n):
    temp=n
    mul=1
    if temp==0:
        print(1)
    elif temp<0:
        print("Enter positive num")
    else:
        for i in range(1,n+1):
            mul=mul*i
    print(mul)
n=int(input("enter the num for factorial :"))
fac(n)
