# Membership operators
"""in: This operator tests if a value is a member of a sequence (e.g., a string, list, or tuple). If the value is a member, it returns True; otherwise, it returns False.
not in: This operator tests if a value is not a member of a sequence. If the value is not a member, it returns True; otherwise, it returns False."""
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the 'in' operator to test if a value is a member of the sequence
if 6 in numbers:
    print("3 is a member of the list 'numbers'.")
else:
    print("not a member of the list 'numbers'.")
# Use the 'not in' operator to test if a value is not a member of the sequence
if 3 not in numbers:
    print("6 is not a member of the list 'numbers'.")
else:
    print("yes!! it is a member of the list 'numbers'.")
