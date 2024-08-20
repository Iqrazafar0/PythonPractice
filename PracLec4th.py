                             #dicts & sets in python

#Q1:Dictionary Operations
#Create an empty dictionary my_dict. Add key-value pairs for "apple" with value 3, "banana" with value 5, and "cherry" with value 7. Print the dictionary.

my_dict ={}
my_dict["apple"] = 3
my_dict["banana"] = 5
my_dict["cherry"] = 7
print(my_dict)

#Q2:Dictionary Access
#Given a dictionary ages = {'John': 25, 'Jane': 30, 'James': 22}, access Jane's age and print it.

ages = {'John': 25, 'Jane': 30, 'Janes': 22}
print(ages['Janes'])

#Q3:Set Operations
#Create two sets set1 and set2 with some common elements. Print their intersection.

set1 = {2,3,4}
set2 = {3,5,1}
print(set1.intersection(set2))

#Q4:Set Manipulation
#Create a set my_set with elements 'a', 'b', 'c'. Add 'd' to the set and print the updated set.

my_set = {'a','b','c'}
my_set.add('d')
print(my_set)

#Q5:Dictionary Iteration
#Iterate over the dictionary grades = {'Alice': 85, 'Bob': 72, 'Charlie': 93} and print each student along with their grade.

grades = {'Alice': 85, 'Bob': 72, 'Charlie': 93}
for student, grade in grades.items():
    print(f"{student}: {grade}")

#Q6:Set Union
#Create two sets setA and setB. Print their union.

setA = {1,2,3}
setB ={3,4,5}
print(setA.union(setB))

#Q7:Dictionary Update
#Update the dictionary info = {'name': 'John', 'age': 30} to include 'city' as 'New York'. Print the updated dictionary.

info =    {'name': 'John', 'age': 30}  
info['city'] = 'new york'
print(info)

#Q8:Set Difference
#Create two sets setX and setY. Print the elements that are in setX but not in setY.

setX = {3,4,5}
setY ={6,3,7}
print(setX.difference(setY))

#Q9:Dictionary Length
#Determine the number of key-value pairs in the dictionary inventory = {'apples': 10, 'bananas': 5, 'oranges': 8} and print it.

inventory = {'apples': 10, 'bananas': 5, 'oranges': 8}
print(len(inventory))

#Q10:Set Removal
#Create a set colors = {'red', 'blue', 'green'}. Remove 'blue' from the set and print the updated set.

colors = {'red', 'blue', 'green'} 
colors.remove('blue')
print(colors)