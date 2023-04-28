# To start a function, you must use the keyword "def".
# Then you will have the name of the function. "multiply" in this case.
# And then you will have parameters, you must still include the () at the end of the function name even if there are no parameters being passed through.
# Functions must have 2 lines seperating them from other lines of code.
def multiply():
    result = 10.5 * 4
    return result

answer = multiply()
print(answer)

# Parameters
def addition(x, y):
    new_result = x + y
    return new_result

# To print it or return the function, you must put in the arguments for the parameters, 6 and 6 in this case.
new_answer = addition(6, 6)
print(new_answer)

# Calling the function elsewhere:
for val in range(1,5):
    adding = addition(4, val) # This will add 4 to each iteration of the loop.
    print(adding)


# Palindromes
# A word that reads the same forwards and backwards. Normally used for fun, but can be used in many projects.

# Here is a function to see if something is a palindrome.

def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards.
    
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()

print(is_palindrome("kayak")) # Returns true


def palindrome_sentece(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.
    The function ignores whitespace, capitalization and puncuation in the sentence.
    
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if palindrome_sentece(word):
    print("'{}' is a palindrome.".format(word))
else:
    print("'{}' is not a palindrome.".format(word))
    

# Funtion using docstrings and fibonacci sequence.

def fibonacci(n: int) -> int:
    """Return the `n`th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0
    
    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
        
    return result


for i in range(36):
    print(i, fibonacci(i))

# Fizzbuzz game

def fizz_buzz(int: int) -> str:
    """
    Fizz Buzz game
    :param int: Any given number
    :return: If the number is divisible by both 3 and 5, return fizz buzz
             If the number is divisible by 3, return fizz
             If the number is divisible by 5, return buzz
             If the number is none of these, return the number.
    """
    if int % 3 == 0 and int % 5 == 0:
        return "fizz buzz"
    elif int % 3 == 0:
        return "fizz"
    elif int % 5 == 0:
        return "buzz"
    else:
        return str(int)


 
for i in range(1, 101):
    print(fizz_buzz(i))