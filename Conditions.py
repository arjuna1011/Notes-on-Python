# AND conditions checks if BOTH conditions are true.
    # TRUE + TRUE == true || TRUE + FALSE = false || FALSE + FALSE = false
age = int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Have a good day at work!")

# OR conditions check if ONE of however many conditions are true.
    # TRUE + FALSE = true || FALSE + FALSE = false || TRUE + TRUE = true

year = int(input("What year were you born? "))

if year >= 1997 or year <= 2012:
    print("You are a zoomer!")


# You can also simplify chained comparisons. Like for an AND statement.
    # age = int(input("How old are you? "))

    # if 16 <= age <= 65:   # This means the same as the AND statement at the start of the page.
        #print("Have a good day at work!")
