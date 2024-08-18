                #practice questions strings

#Q1:Write a function to reverse a given string.

reverse_string = "hello"
print(reverse_string[::-1]) 

#Q2:Write a program that takes a string and a substring as input from the user. Check if the substring exists in the string and
#  print a message accordingly.

string = str(input("Enter the string:"))
sub_string = str(input("Enter the sub_string:"))
if(sub_string in string):
 print("it has substring")
else:
 print("not has substring") 

                    #PRACTICE QUESTIONS CONDITIONAL STATEMENTS

#Q1:Write a program that takes a year as input from the user and prints whether it is a leap year or not.

year = int(input("Enter a year:"))

if (year % 4  == 0 and year % 100 !=0) or (year % 400 == 0):
    print("leap year")
else:
    print("not leap year")   
