# Python 101/ Exercises
#Exercise 1
#Write a python program that:#

# 1-Asks the user about their name
# 2-Save it in a variable called "name"
# 3-Asks the user about their age
# 4-Save it in a variable called "age"
# 5-Print a string stating "The user -name- is -age- years old"
"""
name= input("Enter your full name:  ")
age= input("Enter your age:  ")
print(type(age))
print(f'The user {name} is {age} years old')


input("Press Enter to exit...")
"""
#=====================================================#
#Exercise 2
#Ask the user for a number. Depending on whether the number is even or odd, print 
# out an appropriate message to the user. Hint: how does an even / odd number 
# react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message. 
# Ask the user for two numbers: one number to check (call it num) and one number 
# to divide by (check). If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message.
"""
try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is an even number")

        if num % 4 == 0:
            print(f"{num} is also a multiple of 4")
    else:
        print(f"{num} is an odd number")

    # Extra part
    numx = int(input("Enter a number to be checked: "))
    check = int(input("Enter a number to divide by: "))

    if numx % check == 0:
        print(f"{check} divides evenly into {numx}")
    else:
        print(f"{check} does NOT divide evenly into {numx}")

except ValueError:
    print("Invalid input. Please enter valid integers.")

input("Press Enter to exit...")
"""
#=====================================================#
#Exercise 3
#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.
"""
print("Exercise 3")
newSet = lambda x: [x[0], x[-1]]

#def newSet(a):
#    return [a[0], a[-1]]
    
a= [5, 10, 15, 20, 25]
print(newSet(a))
input("Press Enter to exit...")
"""
#=====================================================#
#Exercise 4
#Write a function that takes an ordered list of numbers (a list where the elements
#  are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and 
# returns (then prints) an appropriate boolean.
"""
def findNum(numst,num):
    nums = sorted(numst)
    print(nums)
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == num:
            return True
        elif nums[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


nums = [4,5,6,7,2,4,8,9,10]
try:
    num =int(input("Enter a number:"))
    if(findNum(nums,num)):
        print(f"{num} is in the list")
    else:
        print(f"{num} is not in the list")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

input("Press Enter to exit...")
"""

#=====================================================#
# ex.2 best practice. 
# Function to get a positive integer from the user
"""
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("That's not a valid integer. Please enter a valid positive integer.")

# Ask the user for a positive integer
n1 = get_positive_integer("Enter a valid positive integer: ")
# Check if the number is a multiple of 4
if n1 % 4 == 0:
    print(f"The number {n1} is a multiple of 4.")
# Check if the number is even or odd
if n1 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Ask the user for 2 positive integer numbers and check if the first number can be evenly divided by the second
num = get_positive_integer("Enter the first positive integer: ")
check = get_positive_integer("Enter the second positive integer: ")
if num % check == 0:
    print(f"The number {num} can be evenly divided by {check}.")
else:
    print(f"The number {num} cannot be evenly divided by {check}.")
"""
#=====================================================#
# ex.3 best practice. 
"""
def finalList(check):
    permanent = []
    # If list length is 2 or less, return the list itself
    if len(check) <= 2:
        permanent = check
        return permanent
    else:
        # Return a new list containing only the first and last elements
        permanent = [check[0], check[-1]]
        return permanent

newList = []

print("Enter numbers to add to list. Press Enter without input to finish.")

while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == '':
        # User chose to finish input
        break
    try:
        num = int(user_input)
        newList.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(f"the original list {newList}")
print(f"the final editted list {finalList(newList)}")
"""
#==========================================
"""
newList = []

print("Please enter list elements ")
while True:
    num = input("Enter number :")
    if num == "":
        break
    num = int(num)
    newList.append(num)
print(newList)

input("Press Enter to exit...")
"""
#==========================================
#================= Medium =================
#==========================================
# Exercise 1
# Write a Python program to find three numbers from an array such that the sum of three numbers
# equal to zero. Input : [-1,0,1,2,-1,-4] Output : [[-1, -1, 2], [-1, 0, 1]] 
# Note : Find the unique triplets in the array.

"""
def three_Sum(num):
    if len(num)<3: return []
    num.sort()
    result=[]
    for i in range(len(num)-2):
        left=i+1
        right=len(num)-1
        if i!=0 and num[i]==num[i-1]:continue
        while left<right:
            if num[left]+num[right]==-num[i]:
                result.append([num[i],num[left],num[right]])
                left=left+1
                right=right-1
                while num[left]==num[left-1] and left<right:left=left+1
                while num[right]==num[right+1] and left<right: right=right-1
            elif num[left]+num[right]<-num[i]:
                left=left+1
            else:
                right=right-1
    return result
 
nums1=[-1,0,1,2,-1,-4]
print(three_Sum(nums1))
input("Press Enter to exit...")
"""
#==========================================
# Exercise 2 in test.py file
#==========================================
# Exercise 3
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False
        
    def checkout(self):
        self.is_checked_out = True
    
    def return_book(self):
        self.is_checked_out = False

    def __str__(self):
         return f"{self.title} by {self.author} ({self.year}) (Checked out: {self.is_checked_out})"




class Library:
    def __init__(self):
        self.collection = []
    
    def add_book(self,book):
        self.collection.append(book)
    
    def list_books(self):
        if not self.collection:
            print("The library is empty.")
            return
        for book in self.collection:
            status = "Checked out" if book.is_checked_out else "Available"
            print(f"{book.title} by {book.author} ({book.year}) - {status}")            
    
    def find_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book
        return None

    def remove_book(self, book):
         if book in self.collection:
             self.collection.remove(book)

    def available_books(self):
        return [book for book in self.collection if not book.is_checked_out]



book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

library = Library()
library.add_book(book1)
library.add_book(book2)

found = library.find_book("1984")

print(f"book found: {found}")
library.list_books()
#print([str(book) for book in library.available_books()])
available = library.available_books()
print("availabel books")
if not available:
    print("No available books.")
else:
    for book in available:
        print(book)

print(f"=====================\n")
input("Press Enter to exit...\n")