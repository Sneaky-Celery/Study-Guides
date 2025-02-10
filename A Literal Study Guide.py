# Author: Sneaky Celery
# A Literal Study Guide

'''This file is a study guide to learn about literals, data types, variables, functions, iterations, and values.
   Several functions are commented out, be deliberate about uncommenting and recommenting lines of code as you go
   through this file to ensure the output is not overwhelming.'''

''' The print() is a built-in function of python and we will be using it to learn about some key concepts for coding and 
    python. First, note that '\' is a special character that tells the interpreter to ignore one following character. 
    There are special characters we can input here to accomplish different things: n=newline, t=tab, and s=space
'''
print("\n")

# Examples of literals assigned to variables.
# Strings
single_quote = 'What is the answer to the ultimate question of life'
double_quote = "the Universe"
triple_quote = '''and 
                    Multi-line
                        strings'''  # Because multi-line strings are everything.
print(single_quote, double_quote, triple_quote)

# We can modify the output of printed values by changing the separators(sep=) and ends(end=)
# Be sure to note the differences and that it prints on a new line.
#print(single_quote, double_quote, triple_quote, sep=', ',end='??? ')

# Numeric literals
# Integers
'''Before you run the print function for integer literals, 
   what do you think the output will look like?'''
decimal_int = 42
binary_int = 0b101010
octal_int = 0o52
hex_int = 0x2A
#print(decimal_int, binary_int, octal_int, hex_int, sep='=')

float_num = 3.14        # In math we often use the term decimal to describe this number, however computers identify these as float-points.
scientific_num = 1.2e3  # 'e' is equivalent to exponential values of x10.
complex_num = 4 + 3j    # Notice we could not use 'x' as this denotes hexidecimal in python and the '3' would throw an error.

# Boolean literals can only be 1 of 2 values
is_python_fun = True
is_coding_hard = False

# Collection literals
# Lists are ordered, mutable, and may contain different types of data
# NOTE: You can uncomment or comment-out multiple lines of code with "Ctrl + /" or "Command + /"

my_list = [1, 2, 3, "Python"]
#for i in my_list: print([i], end=' ') # Default end is usually a new line.

# print() # Remember we changed the end on the last line, this just ensures we start a new line for the next iteration of our list.
# if len(my_list) < 5:    # len() is a length function that can be applied to strings and collections    
#     my_list.append("mutible"), my_list.insert(0, "My new list")     # Ways to add to a list 
#     del my_list[1:-1]   # How to delete index values From:To        This one deletes everything for the 2nd value to the 2nd-to-last
#     my_list.insert(1,"is") 
#     print(" ".join(my_list),end='.')    # This joins the values of the list with spaces which leaves the strings in a readable format

# Tuples are like lists, except they are immutable.
my_tuple = (1, 2, 3, "Python")
#my_tuple[0] = 99       # Uncommenting this will create an error because tuples cannot be changed.

# Dictionaries use Key:Value pairs
my_dict = {"first": "Bat", "last": "man", "age": 42}
# print()
# print(my_dict.keys())
# print(my_dict.values())
# print()

# A special literal
no_value = None
'''What do you think "None" can be used for?'''

# # A summary of variables, values, and literals to view data types.
# data = [10, 3.14, "hello", True, [1, 2, 3], (4, 5), {6, 7}, {"a": 1, "b": 2}, None]
# # Use a dictionary to print the original value and the data type's name.
# for item in data:
#     print(f"Value: {item}  Type: {type(item).__name__}")
# print()

'''
Literals and Values are closely related. 
The main difference is that a literal is fixed and explicitly written in the code
and a Value is the actual data stored in memory when the script/program runs.

Example:
x = 10      # 10 is a literal.
y = x + 5   # The result is a value.
'''

# We talked about built in functions like print(), len(), and type(), but you can create your own functions too!
# def greeting(name):
#     return print(f"Hello, {name}!")
# name = input("What is your name? ")     # input() is another built-in function of python that requires the user to type something
# greeting(name)

# Explore differences between local and global variables
x = 10  # Global Variable
# def modify():
#     x=5 # Local Variable
#     print("Inside function:", x)    
# print("Outside function:", x)   # Globally x is defined as 10
# modify()                        # Locally x is 5 within the function modify()

'''With this comprehensive baseline, you can begin to explore more complex loops, enumeration, conditionals, 
   list comprehensions, and functions with default parameters.'''
