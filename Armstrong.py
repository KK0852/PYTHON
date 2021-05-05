def armstrong(n):
   a=len(str(n)) 
   sum1=0
   temp=n
   while temp>0:
       s=temp%10               
       sum1=sum1+s**a
       temp//=10
   if sum1==n:
       print("The given number",n," is armstrong ")
   else:
       print("It is not Armstrong")
n=int(input("Enter the number to check armstrong number:"))
armstrong(n)
   