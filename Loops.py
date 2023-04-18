# Iterated through a sequence multiple times without the need for human interaction.

parrot = "Nowegian Blue"

# This will iterate through the string for every character it see's.
for character in parrot:
    print(character)


# Ranges
# Ranges will tell a for loop how many times to run. If the range is 1-20, it will run 19 times. The end value DOES NOT get counted.
for i in range(1,20):
    print("i is now {}".format(i))
# If you want this to run 20 times, change the range from 1-20 to 1-21.
# For ranges that start at zero, you can exclude the first value, just write the highest value you want.
# For example, here is a range that counts from 0 to 20.
for r in range(21):
    print("r is now {}".format(r))

# However, if you would like to count up to a number starting from 0 in steps of any number, you must include the 0 as the starting value
for t in range(0, 21, 2):
    print("t is now {}".format(t)) # This will count from 0 to 20 in steps of 2.

# You can do this counting backwards as well. You will have to reverse the start and finish values, and use a negative step.
for e in range(20, -1, -2):
    print("e is now {}".format(e))

# Range with user input example:
age = int(input("How old are you? "))

if age in range(16, 66):
    print("Have a good day at work!")
else:
    print("Enjoy your free time....")

# Nested For loops: These are just for loops that contain another for loop inside of it.

for i in range (1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}.".format(j, i, i * j))
    print("-------------")

# Continue: Tells the loop to end the iteration and to continue with the rest of the loop.
shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shoppingList:
    if item == "spam":
        continue # Stops at "spam" and then continues the loop.

    print("Buy " + item)

# Break: This will end the loop entirely and starts the next line of code.
shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

itemToFind = "spam"
foundAt = None  # This sets the variable as null. 

for index in range(len(shoppingList)):
    if shoppingList[index] == itemToFind:
        foundAt = index 
        break # This will stop the loop once it finds the "spam" string.


print("Item found at position {}".format(foundAt))


# Working with the None variable type.
# We can write the code above in an easier way

itemToFind = "flour"
foundAt = None  # This sets the variable as null. 

if itemToFind in shoppingList: # Is the item in the list?
    foundAt = shoppingList.index(itemToFind)    # Found it at the current index.

if foundAt is not None: # This will look to see if the item is present in the list.
    print("Item found at position {}".format(foundAt))
else: # If it isn't, this will run.
    print("{} not found".format(itemToFind))


# --------------------------------------------------------------------------------------------------------------

# While loops: Functions the same as a For Loop, except we can use it to keep looping as long as a condition remains true. If the condition becomes false, the while loop will break automatically.
# Here is an example:

i = 0 # Everytime the loop iterates, the value of 1 will increase by 1.
while i < 10: # When i gets to 10, the loop will terminate, because 10 is not less than 10.
    print("i is now {}".format(i))
    i += 1 # This is the same as writing i = i + 1. This way is more efficient to use.

# Adventure example:

availableExits = ["north", "south", "east", "west"]

chosenExit = ""
while chosenExit not in availableExits: # If the user keeps inputting a value that is not located in the sequence, this will keep running.
    chosenExit = input("Please choose a direction: ").casefold()

print("Glad you were able to make it out alive.")


# Although a while loop will break automatically, we can still add a break function to it.

chosenExit = ""
while chosenExit not in availableExits: # If the user keeps inputting a value that is not located in the sequence, this will keep running.
    chosenExit = input("Please choose a direction: ").casefold()
    if chosenExit == "quit": # If the user wants to quit, they can input this value and it will cause the loop to break.
        print("Game Over") 
        break # Breaks the loop. This is good because the loop only breaks if the user inputs the correct value, if they want to leave on their own terms, this allows them to.
