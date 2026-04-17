# Bad Python Code - Will fail multiple linters

def bad_function(
# Missing parameters and bad indentation
print("Hello World"  # Missing closing parenthesis

def another_bad_function():
    x = 1
    y = 2
    z = x + y
    # No return statement when expected
    
    # Using deprecated or bad practices
    eval("print('dangerous')")  # Security risk
    
    # Inconsistent spacing
    list = [1,2,3,  4,5]
    
    # Line too long (over 79/88 chars)
    very_long_variable_name_that_exceeds_character_limit = "This string is way too long and should be broken into multiple lines for readability"
    
    # Trailing whitespace (invisible but linter catches it)    
    return 
    
# Missing docstring at module level
import os,sys,json,random  # Multiple imports on one line

# Unused imports
import datetime
import math

# Bad variable name (too short/ambiguous)
a = "something"

# Missing spaces around operators
result=5+3*2

# Class with no docstring and bad naming
class myClass:
    pass

# Function with too many arguments (>5)
def too_many_args(a,b,c,d,e,f,g,h,i,j):
    return a+b+c+d+e+f+g+h+i+j

# Bare except clause
try:
    x = 1 / 0
except:  # ← This is bad - should specify exception type
    pass

# Using 'l' as variable name (confusing with 1)
l = [1, 2, 3]

# No newline at end of file
