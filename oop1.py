                                # oop in python

# Q1: Create a class that takes name & marks of 3 subjects as arguments in the constructor. 
# Then create a method to print the average.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = sum(self.marks)
        print("Hi", self.name, "your average score is:", total / 3)

s1 = Student("Karan", [98, 99, 97])
s1.get_avg()

# Q2: Create an Account class with 2 attributes: balance & account number.
# Create methods for debit, credit, & printing the balance.

class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited.")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited.")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(600)
acc1.credit(200)

# Q3: Class with multiple methods
# Define a class Rectangle with attributes length and width.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
rect = Rectangle(6, 8)
print("Area of rectangle =", rect.area())
print("Perimeter of rectangle =", rect.perimeter())

# Q4: Class with a class variable
# Define a class Circle with a class variable pi set to 3.14.
# Add an instance variable radius and a method area to calculate the area of the circle.

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)
    
circle = Circle(5)
print("Area of the circle =", circle.area())
