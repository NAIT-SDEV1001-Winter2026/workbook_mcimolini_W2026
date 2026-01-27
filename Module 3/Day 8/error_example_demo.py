# SyntaxError - Error in the syntax of our code (the way it's written)
# Generally, missing a : or similar
# Your program won't run if there are syntax errors
variable = 1

# SyntaxError: expected ':'
if variable == 1: # as I've left out the : this is a syntax error
    print("Yay!")

# IndentationErrors - This is when your indenting doesn't match
# Your code may run, but bad things happen.
if variable == 1:
    print("Yay!")
    # IndentationError: unexpected indent
    print("IndentationError") # I have an extra space here, so I get an IndentationError

# NameError - This occurs when you try to use a variable that doesn't exist. Often a typo
# Your code will run, but it will likely crash at some point
number = 4
# NameError: name 'nummber' is not defined. Did you mean: 'number'?
print(f"My number is {number}")

# TypeError - This is when we mix incompatable variable types in an operation 
# eg. Adding a string and an int

num_string = "4"
# TypeError: can only concatenate str (not "int") to str
# Error comment after the : will be specific to what Python thinks you're trying to do.
print(f"{int(num_string) + number}") # num_string is a str and number is an int so this won't work