# An expression that evaluates to either TRUE or FALSE
age = 20
# Age's value of 20 is TRUE, if a statement said the value was different, it'd become FALSE.
name = "Jacob"
# If the value is "Jacob", its TRUE. Any other value and its FALSE

day = "Saturday"
temperature = 42
raining = False


if day == "Saturday" and temperature > 27 and not raining:
    print("Go swimming")
# 'not' is reversing the boolean. not true = FALSE && not false = TRUE
# Since the day is equal to what is defined in the variable, that is TRUE. This is the same for the temperature, as well ast the raining vairable.



if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name: #OR if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")


# If the input value does NOT contain the word "cinema".
activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():     # The .casefold() function just converts the input value to lowercase if the user submitted it as upper case.
    print("But I want to go to the cinema")

