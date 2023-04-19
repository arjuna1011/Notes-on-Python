# Lists are sequences of multiple strings, integers, booleans, etc.
# These are arrays in JS

computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mousemat"
                  ]

for part in computer_parts:
    print(part)

print()
# To access one item in the list, you can grab it by it's index position, x[i].
print(computer_parts[2])

print()
# Lists are mutable, you can change the contents of a list.
# For example, here is adding something to a list.

computer_parts += ["headphones"]
print(computer_parts)

# Another way to add to a list.
a = b = computer_parts # Assigning the list to 2 other variables, you don't have to do this in order to add.
b.append("second monitor") # Appending is another way we can add, instead of just using addition. You can exclude the brackets for this.
print(a)

# How to remove from a list.
b.remove("second monitor")
print(a)

# Alternatively, you can use the .pop function to remmove an item from its index position.
b.pop(1)  # This removes the 2nd item in the list, because remember, the index positions start at 0.
print(a)

# How to view the miniumum and maximum values in a list.

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even)) # Minimum value in even
print(max(even)) # Maximum value in even
print(min(odd))  # Minimum value in odd
print(max(odd))  # Maximum value in odd

print()
# How to view the length of a list or any sequence.

print(len(even))
print(len(odd))

print()
# A way to see how many times a character, or value, appears in a list, string, etc.

print("tenessee".count("e")) # This will count how many 'e' characters are in the string.
print(even.count(2)) # This will count how many times the value 2 is included in the list.


print()

# Example using loops and input:

available_items = ["milk",
                   "apples",
                   "butter",
                   "flour",
                   "potatoes",
                   "eggs"
                   ]

# valid_choices = [str(i) for i in range(1, len(available_items) + 1)]
valid_choices = []
for i in range(1, len(available_items) + 1):
    valid_choices.append(str(i))
# print(valid_choices)
current_choice = "-"
grocery_list = []

while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) -1
        chosen_item = available_items[index]
        if chosen_item in grocery_list:
            print("Removing {}".format(current_choice))
            grocery_list.remove(chosen_item)
        else:
            print("Adding {}".format(current_choice))
            grocery_list.append(chosen_item)            
    else:
        print("Please add options from the list below.")
        for number, item in enumerate(available_items): # The enumerate function just lets you get the index of an element while iterating over a list.
                                                        # This is effective instead of writing something that checks the list each time the loop
            print("{0}: {1}".format(number + 1, item))
    current_choice = input()

print(grocery_list)