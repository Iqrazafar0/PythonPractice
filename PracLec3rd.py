                          #lists and tupal in python

#Q1: Concatenate two lists and print the result.

list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2
print(concatenated_list)

#Q2:Access and print the third element of a tuple

my_tuple = (1,3,6,5,6)
third_element = my_tuple[2]
print(third_element)

#Q3:Replace the second element of a list with a new value.

my_list = ['apple','litchi','banana']
my_list[1] = 'mango'
print(my_list)

#Q4:Find the index of a specific element ('apple') in a list.

my_list = ['apple','litchi','banana']
index = my_list.index('apple')
print(index)

#Q5:Check if a tuple contains a specific element ('apple').

my_tuple = ('apple','litchi','banana')
check = 'apple' in my_tuple
print(check)

#Q6:Remove the last element from a list.

list = [5,8,9,0,8]
list.pop()
print(list)

#Q7:Count occurrences of a particular element ('a') in a tuple.

my_tuple = ('a','f','a','r','y')
count = my_tuple.count('a')
print(count)

#Q8:Sort a list of strings alphabetically.

my_list = ['d','r','w','a','b','c']
my_list.sort()
print(my_list)

#Q9:Create a tuple with a single element.

single_element_tuple = ('iqra',)
print(single_element_tuple)

#Q10:Extend a list with elements from another list.

list1 = [1,3,4]
list2 = [6,7,8]

list1.extend(list2)
print(list1)