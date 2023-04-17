# Basic operations

a = 12
b = 3

# Addition
print(a + b)    #15
# Subtraction
print(a - b)    #9
# Multiplication
print(a * b)    #36
# Division
print(a / b)    #4.0
# Integer Division - rounds down
print(a // b)   #4
# Modulo - shows the ramainder
print(a % b)    #0

print()

# For loop, loops through a function x amount of times
for i in range(1, 4):
    print(i)

# If you want to add variables in the range, you can. You can also use expresions along with them.
# However, if you are dividing, you MUST use the integer division method, as Python does NOT allow floats in the range where an int must be used.
for i in range(1, a//b):
    print(i)
