variable = 1

# SyntaxError - Error in the syntax of our code (the way it's written)
# Generally, missing a : or similar
# Your progam won't run if there are any

# SyntaxError: expected ':'
if variable == 1: # as I've left out the : this is a syntax error
    print("Yay!")

# IndentationError - This is when your indenting doesn't match
# Your code may run, but bad things will happen if it does
if variable == 1:
    print("Yay!!")
    # IndentationError: unexpected indent
    print("Indentation Error") # I have an extra space her, so I get an IndentationError

# NameError - This occurs when you try to use a variable that doesn't exist. Often a type.
# Your code will run, but it will likely crash at some point
number = 4
# NameError: name 'nummber' is not defined. Did you mean: 'number'?
print(f"My number is {number}") # number is spelt incorrectly as nummber

# TypeError - This occurs when you try to mix incompatable variable types in an operation
# eg. Adding a string and an int

num_string = "4"
# TypeError: can only concatenate str (not "int") to str
# Error comment after the : will be specific to what Python thinks you're trying to do.
print(f"{int(num_string) + number}") # Python doesn't know how to combine an int and string, so TypeError