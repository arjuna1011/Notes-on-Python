# Lists are sequences of multiple strings, integers, booleans, etc.
# These are arrays in JS
# Lists are mutable, you can change the contents of a list.

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