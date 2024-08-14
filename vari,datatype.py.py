                         # Variables & data types in python

#Question 1: Write a Python program to swap two numbers using a temporary variable.

#taking input from user
a = int(input("Enter num 1:"))
b = int(input("Enter num 2:"))
#using a temp variable for swping
temp = a #store the value of a in temp
a = b      #assign the value of b to a
temp = b #assign the value of temp(original a)to b
#print the swaped values
print("Ater swaping: a=", a,"b =", b)

#Question 2: Write a Python program to find the area of a rectangle. Take the length and width as input from the user.

#taking input from user
length = float(input("enter length of rectangle:"))
width = float(input("enter width of rectangle :"))
area = length * width
print("The area of rectangle =",area)

#Question 3: Write a Python program that converts Celsius to Fahrenheit. The formula to convert Celsius to Fahrenheit is: F = (C * 9/5) + 32.

Celsius =float(input("Enter temprature in celsius:"))
Fahrenheit =(Celsius * 9/5) + 32
print("tempuratue in fahrenheit =",Fahrenheit)

#Question 4: Write a Python program to check if a given number is even or odd.

num=int(input("enter a number:"))
if num % 2 == 0:
 print("even num:")
else:
 print("odd num:")    

#Question 5: Write a Python program to calculate the square and cube of a number.

num =int(input("enter a num:"))
square = num * num
cube = num * num * num
print("The square is=",square, "The cube is=",cube)

#Question 6: Write a Python program to concatenate two strings and print the result.

str1 =input("Enter the first string:")
str2 =input("Enter the second string:")
concatenate = str1 + " " + str2
print("The concatenate string =",concatenate)

#Question 7: Write a Python program to find the maximum of two numbers using conditional operators.

num1 = float(input("enter 1st num:"))
num2 = float(input("enter 2nd num:"))
if num1 > num2:
    print("num1 is maximum.")
else:
    print("num2 is maximum.")    

#Question 8: Write a Python program to calculate the simple interest. Take principal, rate, and time as input from the user.

P = float(input("enter the principal amount:"))
T = float(input("enter the time period:"))
R = float(input("enter the rate of intrest:"))
SI = P*T*R / 100
print("The simple intrest is = ",SI)

#Question 9: Write a Python program to check if a given number is positive, negative, or zero.

num = int(input("enter the num:"))
if num > 0:
    print("its a positive num.")
elif num < 0:
    print("its a negative num.")
else:
    print("num is equal to zero.")
        
#Question 10: Write a Python program to calculate the sum of the first n natural numbers. Take 'n' as input from the user.

n = float(input("enter the num:"))
natural_nums = n*(n+1) // 2
print("the sum of",n,"natual nums is:",natural_nums)