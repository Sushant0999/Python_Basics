"""
Python Lambda Functions are anonymous functions means that the function is without a name.
As we already know the def keyword is used to define a normal function in Python.
Similarly, the lambda keyword is used to define an anonymous function in Python.
"""

str1 = 'Hello Viking'

# Assigning parameter in lambda funtion
test = lambda str: print(str)

upper = lambda string: string.upper()

# Passing argument in lambda function
test('strx')
print(upper(str1))

# Lambda with list

ages = [13, 90, 17, 59, 21, 60, 5]
ages.sort()
adults = list(filter(lambda age: age > 18, ages))

print(adults)