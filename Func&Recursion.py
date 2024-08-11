                       # functions in python

#Q1:WAP to print the length of a list.(list is the parameter).

#cities = ["khanewal","sahiwal","vehari","lahore","okara","karachi"]
#dramas = ["jannisar","khani","humsafar","eshqiya","parizaad"]

#def print_len(list):
#    print(len(list))

#print_len(cities)
#print_len(dramas)

#Q2:WAF to print the elements of a list in a single line.(list is the parameter)

#family = ["iqra","maryam","chanda","zafar","hamza","nomi"]

#def print_list(list):
#    for item in list:
#        print(item, end=" ")

#print_list(family)

#Q3:WAF to calculate the factorial of a number n.

#def cal_fact(n):
#    fact = 1
#    for i in range(1, n+1):
#        fact *= i
#    print(fact)

#cal_fact(7)

#Q4:WAF to convert USD TO INR.

#def converter(usd_val):
#    inr_val = usd_val * 83
#    print(usd_val, "USD", inr_val,"INR")

#converter(100)

                                     # Homework problem

#Q1:WAF to find the num is even or odd and return an string in output.

#def check_num(n):

#    if n % 2 == 0:
#        print("even")
#    else:
#        print("odd")

#check_num(3)
        
                                   # Recursions in python

#Q1:Write a recursive function to calculate the sum of first n natural numbers.

#def calc_sum(n):
#    if(n == 0):
#        return 0
#    return calc_sum(n-1) + n

#sum = calc_sum(9)
#print(sum)

#Q2:Write a recursive function to print all elements iin a list.
#hint:use list and index as parameter.

#def print_list(list,idx=0):
#    if(idx == len(list)):
#        return
#    print(list[idx])
#    print_list(list, idx+1)

#fruits = ["mango", "apple", "grapes", "banana", "lemon"]

#print(fruits)
