"""Code to provide details about Keywords being used in Python language
Keywords are the reserved words in Python. We cannot use a keyword as a variable name, function name or any other identifier.
They are used to define the syntax and structure of the Python language. In Python, keywords are case sensitive."""

import keyword

# Scenario 1
# Initializing strings for testing the code
sample_1 = "Bangalore"
sample_2 = "else"
sample_3 = "elif"
sample_4 = "true"

print()
print("# Scenario 1")
if keyword.iskeyword(sample_1):
    print("Sample 1 is having keyword reference value")
else:
    print("Sample 1 = ", sample_1)

if keyword.iskeyword(sample_2):
    print("Sample 2 is having keyword reference value")
else:
    print("Sample 2 = ", sample_2)

if keyword.iskeyword(sample_3):
    print("Sample 3 is having keyword reference value")
else:
    print("Sample 3 = ", sample_3)

if keyword.iskeyword(sample_4):
    print("Sample 4 is having keyword reference value")
else:
    print("Sample 4 = ", sample_4)

# Scenario 2
# Explaining True, False, None, and, or, not within Python code
print()
print("# Scenario 2")
print(None == 0)

x = 0
y = 0
print(x == y)

print(True or False)
print(False and True)
print(not True)


# Scenario 3
# Explaining global in Python code
print()
print("# Scenario 3")
var_a = 10

# Function to read variable
def read():
    print("Before modifications - ", var_a)

# Function to change the value of globally defined variable
def mod_1():
    global var_a
    var_a = 20
    print("mod_1() - After modifications - ", var_a)

# Function to change the value of only local variable
def mod_2():
    var_a = 15
    print("mod_2() - After modifications - ", var_a)

# Calling functions defined
read()
mod_1()
read()
mod_2()
read()

# Scenario 4
# Explaining non global in Python code
print()
print("# Scenario 4")
def outer_nonlocal():
    var_b = 5
    def inner():
        nonlocal var_b
        var_b = 10
    inner()
    print("Output after using nonlocal - ", var_b)

outer_nonlocal()

print()
print("# Scenario 5")
print("Providing all keywords in Python language!")
print(keyword.kwlist)
