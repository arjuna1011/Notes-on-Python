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


# Augmented assignments: These are more efficient to use in your code.
# For example, instead of saying "var = var + 1", use "var += 1" and you will get the same answer.

x = 23

# Addition - 24
x += 1
print(x)
# Subtraction -  20
x -= 4
print(x)
# Multiplication - 100
x *= 5
print(x)
# Division - 25
x //= 4
print(x)
# Division - 5.0
x /= 5
print(x)
# Multiplication - 25.0
x **= 2
print(x)
# Modulo - 0.0
x %= 5
print(x)

# x's value will change with each operation. This saves memory over writing it the longer way.


# We can sort lists of numbers by their numerical value.
# You will have to use the sorted() function instead of .sort() like in normal lists.
# This is because the sorted() function returns a new list, without changing the original
numbers = [4.2, 61.2, 1.7, 6.2, 4.1]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)