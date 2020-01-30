"""Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes.
Python treats single quotes the same as double quotes. In Python, Strings are arrays of bytes representing Unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1. 
Square brackets can be used to access elements of the string."""

print()
print("# Scenario 1")
string_for_scenario_one = "GeeksForGeeks-PythonProgramming"
search_pattern = "Geeks"
if search_pattern in string_for_scenario_one:
    print("Search Pattern Available = ", search_pattern)
else:
    print("Search Pattern N/A")

print()
print("# Scenario 2")
python_string_1 = "Hello, how are you doing?"
print("Existing String Value = ", python_string_1)
# Strings are immutable, hence elements of a String cannot be changed once it has been assigned
python_string_1 = "Hello, welcome to GeeksForGeeks portal"
print("Modified String Value = ", python_string_1)

print()
print("# Scenario 3")
string_for_scenario_two = "GeeksForGeeksPythonProgrammingWebsite"
another_pattern_match_for_string_activities = "Python"
if another_pattern_match_for_string_activities in string_for_scenario_two:
    print("Pattern Available & Index Value Starts = ", string_for_scenario_two.index('Py'))
else:
    print("Search Pattern N/A")

print()
print("# Scenario 4")
def check_vowels(driver_string_to_validate, list_of_vowels):
    # casefold helps in ignoring cases
    driver_string_to_validate = driver_string_to_validate.casefold()

    # forms dictionary element with key as vowel
    start_counting_vowels = {}.fromkeys(list_of_vowels, 0)

    # for loop to search/count
    for each_character in driver_string_to_validate:
        if each_character in start_counting_vowels:
            start_counting_vowels[each_character] += 1
    return start_counting_vowels

# driver code
driver_string_to_validate = "Geeks For Geeks Geeks For Geeks Geeks For Geeks"
list_of_vowels = 'aeiou'
print(check_vowels(driver_string_to_validate, list_of_vowels))
