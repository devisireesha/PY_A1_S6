# Find the element with the highest frequency
# Take input from user
arr = input("Enter the array elements separated by spaces: ").split()
arr = [int(i) for i in arr]

# Calculate the frequency of each element
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Find the element with the highest frequency
max_freq = 0
max_elem = None
for k, v in freq.items():
    if v > max_freq:
        max_freq = v
        max_elem = k

# Print the result
print("The element with the highest frequency is:", max_elem)
