# Variables hold value. You can assign strings, integers, booleans, and more to a varaible.

variable = "This is a variable."
print(variable)

integer = 20
print(integer)

boolean = True
print(boolean)

# We can see what the type of each variable is if we just add "type()" inside of our print function. This is like typeof in JS.

# This will print a str
print(type(variable))
# This will print an int
print(type(integer))
# This will print a bool
print(type(boolean))

# One thing about Python that may be an advantage over other languages, is you can reassign variables. Similar to how it'd be in JavaScript, except you don't need to add the "let" to the variable.

variable = "I changed this."
print(variable)
integer = 21
print(integer)
boolean = False
print(boolean)

