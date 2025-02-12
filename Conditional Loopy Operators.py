# Author: Sneaky Celery
# Conditional Loopy Operators

'''In this study guide, we will utilize the previous concepts to contruct more interesting
   functions, conditionals, and loops. Again, several portions are commented-out and in this
   guide it is recommended to be deliberate about what portions of the code you run.
   NOTE: Remeber you can use "Ctrl + /" or "Command + /" to uncomment or recomment large sections of code.'''

print("\n")

# Operators
'''
Operator    Effect                                  Comparison Operators    Meaning       
   +        Addition                                         ==             Equal to
   -        Subtraction                                      !=             Not equal to
   *        Multiplication                                   >              Greater than
   /        Division (floating point)                        <              Less than
   //       Floor Division (integer results)                 >=             Greater than or equal to
   %        Modulus (remainders)                             <=             Less than or equal to
   **       Exponentiation
'''
# Examples of the maths
a, b = 10, 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print()

# Comparison operators will yield Boolean results and are often used in conjunction with conditionals
x = input("Pick a number from 1 to 10: ")   # The '=' is an assignment of value.
# x = int(x)                          # All data captured by input() is considered a string, we need to be aware of data types.
# if x > 5:                           # if statements are conditionals that run sequentially
#     print("x is greater than 5")
# elif x == 5:                        # elif is a way to capture additional possible outcomes
#     print("x is exactly 5")         # '==' is how to find out if something is exactly what you are expecting.
# else: print("x is less than 5")     # else is usually a catch-all within the specified parameters

# Demonstration of comparison output values.
# print(f"Is x greater than or equal to 5? {x >= 5}")
# print(f"Is x less than or equal to 5? {x <= 5}")
# print(f"Is x equal to 5? {x == 5}")
# print()

# Logical Operators are used to combine conditions in conditionals
'''
and - returns true if both conditions are true
or  - returns true if at least one condition is true
not - reverse the boolean value
'''
# p, q = True, False
# print("p = True\nq = False")
# print(f"a and b: {p and q}, both are not True.")
# print(f"a or b: {p or q}, at least one is True.")
# print(f"not a: {not p}, p is reversed for this line.")
# print()

# Operators can be applied to strings as well.
# greeting = "Hello, "
# print(greeting + 'world!')  # Concatenation is the term we use when combining strings.

# repeat = "Ha"
# print(repeat * 3, end='!')  # Multiplication repeats the string the desired number of times.
# print()

# print("apple" == "apple")   # True
# print("apple" != "orange")  # True
# print("apple" < "banana")   # True, 'a' comes before 'b' and strings are based on dictionary order.

# sentence = "They have a cave troll."    # We can use 'in' to identify if a string contains something of interest to us.
# print("cave" in sentence)   # True
# print("spider" in sentence) # False

# We can use operators to create simple conversion functions such as miles to kilometers and vice-versa.
# def distance_conversion():
#     print("Type 'exit' to end.")
#     choice = input("Convert mi -> km or km -> mi? (Type: 'miles' or 'kilometers') ").strip().lower()
#     if choice == 'exit':
#         exit()
#     elif choice == 'miles':
#         miles = float(input("Enter the distance in miles: "))
#         miles_conversion = miles * 1.61
#         print(f"{miles} is {round(miles_conversion,2)} kilometers.")
#     elif choice == 'kilometers':
#         km = float(input("Enter the distance in kilometers: "))
#         km_conversion = km / 1.61
#         print(f"{km} kilometers is {round(km_conversion,2)} miles.")
#     else: print("Invalid input. Choose 'miles' or 'kilometers'")

# while True:
#     distance_conversion()

#########################################################################################################

# Let's apply conditionals and operators to loops
important_facts = [42, "Jurassic Park, greatest movie of all time.", "Avatar: The Last Airbender, greatest kids show of all time.", 
                   "I must not fear.", "DON'T PANIC", "Time is non-linear.", "They have a cave troll."]

index = 0       # Initialize the index for the first while loop.
attempts = 0    # Initialize the failed attempts at the magic word.

# while index < len(important_facts):     # This iterates over the full length of the list and 
#     print(important_facts[index])       # prints out the value of each index,
#     index += 1                          # while ensuring we don't create and index out of bounds error.
# print()

# # NOTE: You will run into an error. We can talk about how to find and correct an error here.
# while "please" not in important_facts:  # We create an infinite loop that compares our list of important facts and looks for the value'please'
    
#     magic_word = input("Ah ah ah, you didn't say the magic word. ") # Request input from the user to guess that magic word.
    
#     if magic_word.lower() == 'exit':    # We can create a manual exit, often useful for menu type loops.
#         print(f"Exiting... You failed {attempts} times.")
#         break   # break is used to force escape from infinite loops
    
#     elif magic_word.lower() == "please":    
#         print("Access Granted")
#         important_facts.append(magic_word.lower())  # The lower() ensures the input condition can match the loop requirements.
#         print(f"It took you {attempts} attempts to figure out the magic word.")
    
#     else: 
#         attempts += 1
#         print(f"Failed attempt #{attempts}")
#         # Lastly, let's use enumerate() to dynamicly check for a value that contains the reference for the correct answer.
#         if attempts == 5:
#             # next() finds the first index where 'movie' appears in the list.
#             # enumerate() adds a counter index to an iterable, returning each item with its corresponding index as a tuple.
#             movie = next(i for i, fact in enumerate(important_facts) if 'movie' in fact)  
#             # Retrieve and print the fact containing 'movie' using the found index.  
#             print(f"You should watch the greatest movie of all time == {important_facts[movie] }.") 
#             break                                                                                   