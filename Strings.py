# Printing is essentially console.logging in JS. This just prints a string, variable, etc into the terimnal.
print("hello world")
print('This is my first Python project')
print(1 + 2 + 3 + 4 * 2 * 12 / 2)
print("This is awesome")

# # Combining strings using concatonation.
# greeting = "Salutaions"
# name = input("Please enter your name ")
# print (greeting + "," + " " + name)

# Example of an f-string, this is essentially a template literal from JS, allows you to avoid string concatonation.
greeting = "Salutations"
name = input("Please enter your name ")
print(f"{greeting}, {name}")

# This is an escape character that allows you to split a string over several lines if needed without having to actually split the code.
splitString = "This string has been\nsplit\nover\nseveral lines\n"
print(splitString)

# This is an escape character that allows you to add tab spaces in your string without actually tabbing, avoiding clunkiness.
tabString = "One\tTwo\tThree\tFour\tFive"
print(tabString)

# These correct errors when having multiple quotions
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

anotherSplitString = """This string has been 
split over 
several 
lines"""
print(anotherSplitString)

# A couple of ways to fix errors when using backslashes that aren't meant for escape characters.
print("C:\\Users\\timbulchaka\\notes.txt")
# or
print(r"C:\Users\timbulchaka\notes.txt")

# If you would like to print a character of a string, you can use the index position.
variable = "variable"
# This will print the 4th index position, in this case this would be 'a'. The range starts at 0.
print(variable[4])

print()
# You can use the index position to create word challenges like the one below.
parrot = "Norwegian Blue"
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
# This above prints "we win"

print()
# You can do this with negative indexing as well. -1 starts at the end of the string, -14 is the beggining.
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
# You can just subtract the positive indexing with the amount of characters in the string, for this case, subtract by 14.
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()
# You can use a range for an index position too. If you only want to see the first 5 characters, just do this.
print(parrot[0:5])

# This is called slicing, because you are basically creating a slice in your string. You must have the colon.
# This is creating a slice in the string, that'll only print the word "Blue".
print(parrot[10:14])
print(parrot[:6])   # This will slice everything up to the 6th index position.
# This will slice everything from the 6th index posiiton and onward.
print(parrot[6:])
print(parrot[:])    # This will just print the whole word, "Norwegian Blue".
# This also prints the whole word, "Norwegian Blue".
print(parrot[:6] + parrot[6:])

print()
# You can add "steps" to your slicing. If you want to slice the 0th to 6th index positions, but you want to do it in steps of 2.
# This returns "nre", because its going to the 6th index position in steps of 2.
print(parrot[0:6:2])

number = "9,223,372,046,854,775,807"
# This will go through everything from the 1st index position onward in steps of 4.
print(number[1::4])

# You can also slice backwards using steps.
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]  # zyxwvutsrqponmlkjihgfedcb
# This will print the letters of the alphabet backwards, but won't include 'a'.
print(backwards)
# To include 'a', you will have to write it like this.
backwards = letters[25:-27:-1]  # zyxwvutsrqponmlkjihgfedcba
# or
backwards = letters[25::-1]  # zyxwvutsrqponmlkjihgfedcba
# or
backwards = letters[::-1]  # zyxwvutsrqponmlkjihgfedcba
print(backwards)

print()
# More examples of slicing.
qpo = letters[16:13:-1]
print(qpo)  # Will print 'qpo'.
edcba = letters[4::-1]
print(edcba)    # Will print 'edcba'.
lastEight = letters[25:17:-1]
print(lastEight)    # Will print the last 8 characters, 'zyxwvuts'.


print()
# String replacement fields
age = 24
print("My age is {0} years old.".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}."
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}."
      .format(28, 30, 31))


print()
# String Formatting
for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    
    
# You can sort strings as well.
pangram = "The quick brown fox jumps over the lazy dog."

characters = sorted(pangram) # This will sort the list
# You can replace the variable name with just a string literal, if you don't have a variable to call on.
print(characters) # This will log the sorted list
# The thing about sorting strings is it will sort it based on this order
# spaces -> puncuation and symbols -> Capitals -> lowercase
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', 'T', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 
# 'f', 'g', 'h', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 
# 's', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z']
