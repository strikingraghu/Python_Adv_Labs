"""Code to provide details about Keywords being used in Python language"""
import keyword

# Initializing strings for testing the code
sample_1 = "Bangalore"
sample_2 = "else"
sample_3 = "elif"
sample_4 = "true"

print()
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

print()
print("All validations are done!")
