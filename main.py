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
# Function to get a positive integer from the user
# ex.2 best practice. 
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