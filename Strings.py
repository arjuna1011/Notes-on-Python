# Printing is essentially console.logging in JS. This just prints a string, variable, etc into the terimnal.
print ("hello world")
print ('This is my first Python project')
print (1 + 2 + 3 + 4 * 2 * 12 / 2)
print ("This is awesome")

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