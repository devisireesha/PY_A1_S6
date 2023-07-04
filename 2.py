# Top two maximum number in array
# Take input from user
arr = input("Enter the array elements separated by spaces: ").split()
arr = [int(i) for i in arr]

# Initialize variables to store the top two maximum numbers
max1 = max2 = float('-inf')

# Loop through each element in the array
for num in arr:
    # Update the top two maximum numbers if a higher number is found
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

# Print the top two maximum numbers
print("The top two maximum numbers are:", max1, max2)
