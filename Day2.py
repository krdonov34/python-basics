# Lists
#friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"] # Lists are ordered and mutable. You can store strings, numbers, booleans, and other lists.
#print(friends[0])

# List Functions
#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#friends.append("Creed") # Adds an element to the end of the list.
#friends.extend(lucky_numbers) # Extends the list by adding the elements of the second list to the first list.
#friends.insert(1, "Kelly") # Inserts an element at a specific index.
#friends.remove("Jim") # Removes an element from the list.
#friends.clear() # Removes all elements from the list.
#friends.pop() # Removes the last element from the list.
#friends.sort() # Sorts the list in ascending order.
#friends.reverse() # Reverses the list.
#print(friends)

# Tuples
#coordinates = (4, 5) # Tuples are ordered and immutable (can't be modified). You can store strings, numbers, booleans, and other tuples.
#coordinates[1] = 10 # This will throw an error because tuples are immutable.
#print(coordinates[0])
#coords = [(1, 2), (3, 4), (5, 6)] # You can store tuples in a list.

# Functions: collection of code that performs a specific task.
#def say_hi(name, age): # def is the keyword to define a function.
#    print("Hello " + name + ", you are " + str(age) + " years old.")

#say_hi("Mike", 35)
#say_hi("Steve", 25)

# Return Statement: returns a value to the caller.
#def cube(num):
#    return num*num*num # Now it will return whatever value comes from the left so that you can view it in the terminal.

#result = cube(4)
#print(result)

# IF Statements: used to check if a condition is true or false.
#is_male = True
#if is_male: # If the condition is true, the code block will be executed.
#    print("You are a male.")
#else: # If the condition is false, the code block will be executed.
#    print("You are not a male.")

# Multiple Conditions IF Statements
#is_male = True
#is_tall = False
#if is_male and is_tall: # AND is used to check if both conditions are true.
#    print("You are a tall male.")
#elif is_male and not(is_tall): # NOT is used to check if the condition is false.
#    print("You are a short male.")
#elif not(is_male) and not(is_tall):
#    print("You are not a male but are tall.")
#else: # If the condition is false, the code block will be executed.
#    print("You are either not male or not tall.")

# If Statements and Comparisons
#def max_num(num1, num2, num3):
#    if num1 >= num2 and num1 >= num3:
#        return num1
#    elif num2 >= num1 and num2 >= num3:
#        return num2
#    else:
#        return num3
#print(max_num(3,4,5))
# != is used to check if the value is not equal to the value.
# == is used to check if the value is equal to the value.
# >= is used to check if the value is greater than or equal to the value.
# <= is used to check if the value is less than or equal to the value.
# > is used to check if the value is greater than the value.
# < is used to check if the value is less than the value.
# "and is" used to check if both conditions are true.
# "or is" used to check if either condition is true.
# "not is" used to check if the condition is false.

# Dictionaries: allows you to store information in key-value pairs.
#monthConversions = {
#    "Jan": "January",
#    "Feb": "February",
#    "Mar": "March",
#    "Apr": "April",
#}
#print(monthConversions["Jan"])
#print(monthConversions.get("Dec")) # .get is used to get the value of a key.

# While Loops: used to loop through a block of code multiple times.
#i = 1
#while i <= 10:
#    print(i)
#    i = i + 1 # This is the same as i += 1.
#print("Done with loop")

# Building a Guessing Game
#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#out_of_guesses = False
#guess_limit = 3

#while guess != secret_word and not(out_of_guesses):
#    if guess_count < guess_limit:
#        guess = input("Enter guess: ")
#        guess_count += 1
#        print("You have " + str(3 - guess_count) + " guesses left!")
#    else:
#        out_of_guesses = True

#if out_of_guesses:
#    print("Out of guesses, YOU LOSE!")
#else:   
#    print("You win!")

# For Loops: used to loop through a block of code a specific number of times.
#for letter in "Giraffe Academy": # For every letter in giraffe academy I want to print out the letter.
#    print(letter)

friends = ["Jim", "Karen", "Kevin"] 
for index in range(len(friends)): # For every index in the range of the length of the list I want to print out the friend at that index.
    print(friends[index]) # Print out the friend at that index.
