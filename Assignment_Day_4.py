#Assignment Day 4


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
