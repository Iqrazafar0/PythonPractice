                            #  File I/O in python

#Q1:Create a new file "practice.txt" using python.Add the following data in it.

Hi everyone
we are learning file i/o
using java
i like peogramming in java

with open("practice.txt","w") as f:
    f.write("hi everyone\nWe are learning i/o\n")
    f.write("using java\nI like programming in java")

#Q2:WAF that replace the ocurance of java with python in above file.

with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#Q3:Search the word "learnig" is exit in aove file.

word = "learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

#Q4:From a file containing nums separated by comma,print the count of the even nums.

count = 0
with open("practice.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(nums) % 2 == 0):
            count += 1

print(count)