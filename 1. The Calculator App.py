# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.


def addition(nums):
    if len(nums) < 2:
        raise TypeError("addition() requires at least 2 numbers")
    return(sum(nums))

def subtraction(nums):
    if len(nums) < 2:
        raise TypeError("subtraction() requires at least 2 numbers")
    total = nums[0]
    for i in range(1,len(nums)):
        total-=nums[i]
    return total

def multiplication(nums):
    if len(nums) < 2:
        raise TypeError("multiplication() requires at least 2 numbers")
    total = nums[0]
    for i in range(1,len(nums)):
        total*=nums[i]
    return total

def division(nums):
    if len(nums) < 2:
        raise TypeError("division() requires at least 2 numbers")
    total = nums[0]
    for i in range(1,len(nums)):
        total/=nums[i]
    return total


# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

operation = input("What operation would you like to do? (addition, subtraction, multiplication, division)")

if operation.lower() == "addition":
    numbers = input("Please Enter Your Numbers Separated By Space")
    number_array=numbers.split()
    converted = [int(num) for num in number_array]
    print("The Answer Is: ",addition(converted))
elif operation.lower() == "subtraction":
    numbers = input("Please Enter Your Numbers Separated By Space")
    number_array=numbers.split()
    converted = [int(num) for num in number_array]
    print("The Answer Is: ",subtraction(converted))
elif operation.lower() == "multiplication":
    numbers = input("Please Enter Your Numbers Separated By Space")
    number_array=numbers.split()
    converted = [int(num) for num in number_array]
    print("The Answer Is: ",multiplication(converted))
elif operation.lower() == "division":
    numbers = input("Please Enter Your Numbers Separated By Space")
    number_array=numbers.split()
    converted = [int(num) for num in number_array]
    print("The Answer Is: ",division(converted))
else:
    raise ValueError("Not a valid operation.")


