#ex1
class StringManipulator:
     def __init__(self):
         self.string = ""
     def getString(self):
         self.string = input()
     def printString(self):
         print(self.string.upper())

#ex2
class Shape:
     def area(self):
         return 0
class Square(Shape):
     def __init__(self, length):
         self.length = length
     def area(self):
         return self.length ** 2
#ex3
class Shape:
     def area(self):
         return 0
class Rectangle(Shape):
     def __init__(self, length, width):
         self.length = length
         self.width = width
     def area(self):
         return self.length * self.width

#ex4
import math
class Point:
     def __init__(self, x, y):
         self.x = x
         self.y = y
     def show(self):
         print(f"({self.x} , {self.y})")
     def move(self, new_x, new_y):
         self.x = new_x
         self.y = new_y
     def dist(self, other_point):
         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#ex5
class Account:
     def __init__(self, owner, balance):
         self.owner = owner
         self.balance = balance

     def deposit(self, amount):
         self.balance += amount
     def withdraw(self, amount):
         if amount <= self.balance:
             self.balance -= amount
             print(f"You have {self.balance} on your account")
         else:
             print("Funds unavailable!")

#ex6
nums = []
s = input()
nums = s.split(" ")
nums = [int(i) for i in nums]
prime_nums = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False, nums))
print("Prime numbers:", prime_nums)