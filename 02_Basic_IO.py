"""Developers often have a need to interact with users, either to get data or to provide some sort of result.
Most programs today use a dialog box as a way of asking the user to provide some type of input.
While Python provides us with two inbuilt functions to read the input from the keyboard.
raw_input ( prompt )
input ( prompt )

raw_input ( ) : This function works in older version (like Python 2.x).
This function takes exactly what is typed from the keyboard, convert it to string and then return it to the variable in which we want to store.

input ( ) : This function first takes the input from the user and then evaluates the expression, which means Python automatically identifies whether user entered a string or a number or list.
If the input provided is not correct then either syntax error or exception is raised by python."""

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
