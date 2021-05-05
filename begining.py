//Append

num=[]
num.append(5)
num.append(5.6)
num.append('hello')
print(num)

//ascii value

c=input("enter the any letter:")
print(ord(c))

//simple interest

def sim(p,t,r):
    si=(p*r*t)/100
    return si
    
a=int(input("enter p:"))
b=int(input("enter r:"))
c=int(input("enter t:"))
print(sim(a,b,c))

//prime number

a=int(input("enter start:"))
b=int(input("enter end:"))
for i in range(a,b):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
             print(i)