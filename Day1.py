# Day 1
print("Hello World") #Print text
# Drawing a shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Variables and Data Types
# Variables: A container where you can store certain data values.
# String: Plain Text, closed by quotation marks
character_name = "Keagan"
# Boolean: Numbers Essentially
# character_age = 22.8
character_age = "22"
# True and False Statements
is_male = True
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
# Variables can be reset later in the code to mean something different later on.
character_name = "Sydney"
print("He really liked the name " + character_name + ",")
print("but he didn't like being " + character_age)

# Working with Strings
print("Giraffe\nAcademy") # \n returns the following text to the next line.
print("Giraffe\"Academy") # \" allows you to input a " without ending the string.
phrase = "Giraffe Academy"
print(phrase + " is cool.") # Concatenating Strings (bringing them together).
print(phrase.lower()) # Function that converts whole string to lowercase.
print(phrase.isupper()) # Function that checks if whole string is uppercase.
print(phrase.upper().isupper()) # Function within a function.
print(len(phrase)) # Checks the length of the phrase by characters.
print(phrase[0]) # Grabbing characters from a string using indexing (0 is the first character and so on).
print(phrase.index("G")) # Indexes to find our parameter "G".
print(phrase.index("Acad")) # Indexes to find where our parameter "Acad" starts.
print(phrase.replace("Giraffe", "Elephant"))

#Working with Numbers
print(2) #Print a number.
print(3+4.5) # Addition.
print(3*4) # Multiplication.
print(3 + 4 * 5) # Follows order of operations (PEMDAS).
print(3 * (4 + 5)) # Unless otherwise noted via parantheseis.
print(10 % 3) # Modulus Function: Divides the numbers and provides the remainder, so 10/3 = 9 therefore we get a remainder of 1 as the output.
my_num = 5 # Setting variables and printing.
print(my_num)
print(str(my_num) + " is my favorite number.") #Converting number to string --> comes in handy when you want to print numbers alongside strings.
print(abs(my_num)) # ABS: Absolute value function.
print(pow(3, 2)) # POW: takes 3 raised to the power of 2.
print(max(3, 2)) # MAX and MIN: determines the max or min of the numbers.
print(round(3.7)) # ROUND: rounds the number to the closest whole number.
from math import * # Goes out and grabs math functions we can use.
print(floor(3.7)) # Grabs the lowest whole number.
print(ceil(3.7)) # Grabs the highest whole number.
print(sqrt(36)) # Square roots the number.

# Getting input from users.
#name = input("Enter your name: ") # Asking the user for input and storing the value the user inputs as "name".
#age = input("Enter your age: ")
#print("Hello " + name + "! You are " + age + ".")

# Building a Basic Calculator
#number1 = input("Enter a number: ") # int = turns a string into a whole number
#number2 = input("Enter another number: ") # float = turns a string into a decimal number
#result = float(number1) + float(number2)
#print(result)