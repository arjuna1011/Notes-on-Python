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

lynyrd = ("Second Helping", "Lynyrd Skynyrd", 1974)
print(lynyrd)
# lynyrd[0] = "Sweet Home Alabama" # Tuples will not allow the data to be changed.
print(lynyrd)
lynyrd2 = list(lynyrd)
print(lynyrd2)
lynyrd2[0] = "Sweet Home Alabama" # A list, however, will allow the data to be changed.
print(lynyrd2)

# Unpacking a tuple. 
a = b = c = d = e = f = 12 # All varaibles are assigned the value 12.
print(c) 

x, y, z = 1, 2, 6 # x is bound to the 1 value, y is bound to the 2 value, and z is bound to the 6 value.
# The 1,2,6 is the tuple, in this case, and assigning them to different variables is called unpacking a tuple.

# Can also be written like this
data = 2, 4, 10 # Data is the tuple in this case
a, b, c = data # Unpacking it by assigning each value to different variables.

# Another way of unpacking tuples.

for t in enumerate("abcdefg"):
    index, character = t
    print(index, character)
    
# More unpacking

title, artist, year = lynyrd
print(title)
print(artist)    
print(year)    

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride The Lightning", "Metallica", 1984)
          ]
print(len(albums)) # If we didn't put each entry in the parentheses, we would get 15 instead of 5.

for album in albums: # For each value in the list.
    name, artist, year = album # Unpacks the tuple into new variables.
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

# or

# This is the more efficient method, but there are advantages to keeping the original tuples alone.
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))