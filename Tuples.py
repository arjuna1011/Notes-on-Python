# Tuples are a sequence type similar to lists, but they are recognized by parentheses instead of brackets.

t = "a", "b", "c"
print(t)
u = ("a", "b", "c")
print(u)

# When parentheses are needed. Must be used when you are passing a tuple as a function argument.
name = "Jacob"
age = 19

print(name, age, "Python", 2023) # This is the incorrect way.
print((name, age, "Python", 2023)) # This is the correct way.

# Unlike lists, tuples are immutable. You can't change the values.
# Tuples use less memory than lists, so that's one reason why you might use them.
# The immutability of tuples makes them good for protecting data.

lynyrd = "Second Helping", "Lynyrd Skynyrd", 1974
print(lynyrd)
lynyrd[0] = "Sweet Home Alabama" # Tuples will not allow the data to be changed.
print(lynyrd)
lynyrd2 = list(lynyrd)
print(lynyrd2)
lynyrd2[0] = "Sweet Home Alabama" # A list, however, will allow the data to be changed.
print(lynyrd2)