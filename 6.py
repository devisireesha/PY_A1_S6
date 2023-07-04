# Count occurrence of vowels and consonants
def count_vowels_consonants(string):
    vowels = 'aeiou'
    num_vowels = 0
    num_consonants = 0
    for char in string.lower():
        if char in vowels:
            num_vowels += 1
        elif char.isalpha():
            num_consonants += 1
    return num_vowels, num_consonants

# Take input from user
string = input("Enter a string: ")

# Call the function to count vowels and consonants
num_vowels, num_consonants = count_vowels_consonants(string)

# Print the results
print("Number of vowels:", num_vowels)
print("Number of consonants:", num_consonants)
