"""Developers often have a need to interact with users, either to get data or to provide some sort of result.
Most programs today use a dialog box as a way of asking the user to provide some type of input.
While Python provides us with two inbuilt functions to read the input from the keyboard.
raw_input ( prompt )
input ( prompt )

raw_input ( ) : This function works in older version (like Python 2.x).
This function takes exactly what is typed from the keyboard, convert it to string and then return it to the variable in which we want to store.

input ( ) : This function first takes the input from the user.
It then evaluates the expression, which means Python automatically identifies whether user entered a string or a number or list.
If the input provided is not correct then either syntax error or exception is raised by python.

Developer often wants a user to enter multiple values or inputs in one line.
In C++/C user can take multiple inputs in one line using scanf but in Python user can take multiple values or inputs in one line by two methods.

Using split() method
Using List comprehension

Using split() method :
This function helps in getting a multiple inputs from user . It breaks the given input by the specified separator.
If a separator is not provided, then any white space is going to be a separator.
Generally, user use a split() method to split a Python string. But, one can also use it in taking multiple input as well.

Using List comprehension :
List comprehension is an elegant way to define and create list in Python.
We can create lists just like mathematical statements in one line only.
It is also used in getting multiple inputs from a user.

By default python’s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without newline.
Python’s print() function comes with a parameter called ‘end’. 
By default, the value of this parameter is ‘\n’, i.e. the new line character. 
You can end a print statement with any character/string using this parameter.

The separator between the arguments to print() function in Python is space by default (softspace feature).
Which can be modified and can be made to any character, integer or string as per our choice.
The ‘sep’ parameter is used to achieve the same, it is found only in python 3.x or later. It is also used for formatting the output strings."""

print()
print("# Scenario 1")
get_input_value_from_user = input("Enter your name = ")
if type(get_input_value_from_user) == str:
    print("Details entered in the prompt = ", get_input_value_from_user)
else:
    print("Please enter string value only!")

print()
print("# Scenario 2")
get_value_from_an_end_user_1 = int(input("Enter the number you like = "))
get_value_from_an_end_user_2 = float(input("Enter float type number = "))
get_value_from_an_end_user_3 = str(input("Enter the string you like = "))
print("Results - ")
print("Integer input received = ", get_value_from_an_end_user_1)
print("Float input received = ", get_value_from_an_end_user_2)
print("String input received = ", get_value_from_an_end_user_3)

if type(get_value_from_an_end_user_1) == int:
    print("Moving the value type from Int to Float within this code")
    move_to_float_type = float(get_value_from_an_end_user_1)
    print(move_to_float_type)
else:
    print("Please enter correct details")

print()
print("# Scenario 3")
user_input_1, user_input_2 = input("Enter any 2 numbers = ").split()
print("Enter values by user in input_1 = ", user_input_1)
print("Enter values by user in input_2 = ", user_input_2)

get_multiple_values_from_end_user = list(map(int, input("Enter multiple numbers in this prompt = ").split()))
print("All values provided by an end user = ", get_multiple_values_from_end_user)

print()
print("# Scenario 4")
get_user_value_x, get_user_value_y = (int(x) for x in input("Enter 2 int values = ").split())
print("Display value X = ", get_user_value_x)
print("Display value X = ", get_user_value_y)

get_users_value_for_x, get_users_value_for_y = (int(x) for x in input("Enter 2 integers = ").split())
print("Final Output | X = {}, Y = {}".format(get_users_value_for_x, get_users_value_for_y))

print()
print("# Scenario 5")
demo_of_end_variable_1 = "GeeksforGeeks"
demo_of_end_variable_2 = "Bangalore"
print(demo_of_end_variable_1, end=" ")
print(demo_of_end_variable_2, end=" ")
demo_of_end_variable_3 = "PythonCoding"
demo_of_end_variable_4 = "DjangoCoding"
print(demo_of_end_variable_3, sep=" ")
print(demo_of_end_variable_4, sep=" ")
demo_of_end_variable_5 = "Server Side Coding"
demo_of_end_variable_6 = "Client Side Coding"
print(demo_of_end_variable_5, demo_of_end_variable_6, sep="-")
