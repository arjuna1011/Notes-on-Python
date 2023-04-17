name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age);

# Basic if statement, allows you to check a certain condition. If they don't meet the condition, the else statement then runs.
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.... Please come back in {0} years.".format(18 - age))

# Elif is used for more than 2 conditions. Just stands for Else If.
if age < 18:
    print("You are not old enough to vote.... Please come back in {0} years.".format(18 - age))
elif age == 200:
    print("You are way too old!")
else:
    print("You are old enough to vote!")

# Guessing game example:
answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

# if guess < answer: # If the guess is less than the answer
#     print("Please guess higher.") 
#     guess = int(input())
#     if guess == answer: 
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you were incorrect.")
# elif guess > answer:   # If the guess is greater than the answer
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you were incorrect.")
# else:   # If the answer is correct
#     print("Well done, you guessed it!")

# Or 

if guess == answer:
    print("You got it first time!")
else:
    if guess < answer:
        print("Please guess higher.")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You got it correct!")
    else:
        print("Sorry, you are incorrect!")