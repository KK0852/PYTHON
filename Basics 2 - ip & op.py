####INPUT
# #input ( ) : This function first takes the input from the user
#input from user


val = input("Enter your value: ")
print(val)

"""Whatever you enter as input, input function convert it into a string. 
if you enter an integer value still input() function convert it into a string"""

# Program to check input
# type in Python

num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))


"""raw_input ( ) : This function works in older version (like Python 2.x).
 This function takes exactly what is typed from the keyboard, 
 convert it to string and then return it to the variable in which we want to store. """

 # Python program showing
# a use of raw_input()

g = raw_input("Enter your name : ")
print g


####Typecasting
#Typecasting the input to Integer:

# input
num1 = int(input())
num2 = int(input())

# printing the sum in integer
print(num1 + num2)


#Typecasting the input to String

# input
string = str(input())

# output
print(string)

#Taking multiple input 


# Python program showing how to
# multiple input using split

# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking two inputs at a time
a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)


# input using list comprehension
"""List comprehension is an elegant way to define and create list in Python. 
We can create lists just like mathematical statements in one line only. 
It is also used in getting multiple inputs from a user."""


# Python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three value: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
print()

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First number is {} and second number is {}".format(x, y))
print()

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)



# ###raw input will take the input as string

# Python 2.x program to show differences between
# input() and rawinput()function

# 3 inputs using raw_input() function,
# after which data type of the value
# entered is displayed
s1 = raw_input("Enter input to test raw_input() function: ")
print type(s1)

s2 = raw_input("Enter input to test raw_input() function: ")
print type(s2)

s3 = raw_input("Enter input to test raw_input() function: ")
print type(s3)

# 3 inputs using input() function,
# after which data type of the value
# entered is displayed
s4 = input("Enter input to test input() function: ")
print type(s4)

s5 = input("Enter input to test input() function: ")
print type(s5)

s6 = input("Enter input to test input() function: ")
print type(s6)

######print()
"""Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)
Parameters: 
value(s) : Any value, and as many as you like. Will be converted to string before printed 
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘ 
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’ 
file : (Optional) An object with a write method. Default :sys.stdout 
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
Returns: It returns output to the screen."""


# This line will automatically add a new line before the
# next print statement
print ("GeeksForGeeks is the best platform for DSA content")

# This print() function ends with "**" as set in the end argumennt.
print ("GeeksForGeeks is the best platform for DSA content", end= "**")


b = "for"

print("Geeks", b , "Geeks")

#sep and end in print()

# Python 3.x program showing
# how to print data on
# a screen

# One object is passed
print("GeeksForGeeks")

x = 5
# Two objects are passed
print("x =", x)

# code for disabling the softspace feature
print('G', 'F', 'G', sep ='')

# using end argument
print("Python", end = '@')
print("GeeksforGeeks")


# Python 3 code for printing
# on the same line printing
# geeks and geeksforgeeks
# in the same line

print("geeks", end =" ")
print("geeksforgeeks")

# array
a = [1, 2, 3, 4]

# printing a element in same
# line
for i in range(4):
	print(a[i], end =" ")


#####OUTPUT formatting

# Python program showing
# use of format() method

# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and refering
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))


# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

# using format() method and refering
# a position of the object
print(f"{'Geeks'} and {'Portal'}")
