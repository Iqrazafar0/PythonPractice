                 #Strings in python

#Q1:WAP to input user's first name and print its length.

name = str(input("Enter your name:"))
print("The length of your name is=",len(name))

#Q2:WAP to find the occurance of '$' a string.

str = "The rate of $ is increace this month as compare to the last month.Hoping that $ rate will increace in coming days."
print("The occurance of $ sign is =",str.count("$"))

                 #Conditional statements in python

#Q1:WAP to check if the number is even or odd.

num = int(input("Enter the num:"))

if(num % 2 == 0):
    print("even")
else:
    print("odd")

 #Q2:WAP to  find the greatest number entered by the user.

a = int(input("Enter the 1st num:"))
b = int(input("Enter the 2nd num:"))
c = int(input("Enter the 3rd num:"))

if(a>=b & a>=c):
    print("A is greater num.",a)
elif(b>=c):
    print("B s greater num.",b)
else:
    print("C is greater num.",c)

#Q3:WAP to check that the entered num is multiple of '7' or not.

a = int(input("Enter a num:"))

if( a % 7 ==0):
    print("multiple of seven.")
else:
    print("not a multiple.")

                   #Home Task

#Q1:WAP to find a geatest num from the '4' entered nums.

a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))
c = int(input("Enter 3rd num:"))
d = int(input("Enter 4th num:"))

if(a>b & a>c & a>d):
    print("a is greater.",a)
elif(b>c & b>d):
    print("b is greater.",b)
elif(c>d):
    print("c is greater.",c)
else:
    print("d is greater.",d)    
