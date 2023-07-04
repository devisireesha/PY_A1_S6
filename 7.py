# Sum of Digits of a number
def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum

# Take input from user
num = int(input("Enter a number: "))

# Call the function and print the result
result = sum_of_digits(num)
print("The sum of digits of", num, "is:", result)
