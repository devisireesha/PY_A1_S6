# Sort elements in Python Dictionary
# Create a dictionary
my_dict = {'c': 1, 'b': 2, 'a': 3}

# Sort the dictionary by keys
sorted_dict = {}
for key in sorted(my_dict.keys()):
    sorted_dict[key] = my_dict[key]

# Print the sorted dictionary
print(sorted_dict)

# Create a dictionary
my_dict = {'c': 1, 'b': 2, 'a': 3}

# Sort the dictionary by values
sorted_dict = {}
for key, value in sorted(my_dict.items(), key=lambda x: x[1]):
    sorted_dict[key] = value

# Print the sorted dictionary
print(sorted_dict)

