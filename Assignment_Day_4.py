# Assignment Day 4
# Edit: Added Assignment Question
# Day 4 Assignment:
# Define a function which will take a number as argument and return its factorial.
# Call the function to print factorial of any number(integer).

#Function
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

#Taking Input
value = int(input("Enter an integer: "))

#Calling Function
print("Factorial of", value, "is :", fact(value))


# Notes 
# expected 2 blank lines after class or function definition in python
