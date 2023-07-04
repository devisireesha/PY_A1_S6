# To find GCD or HCF of two numbers
import math

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compute GCD of the two numbers
gcd = math.gcd(num1, num2)

# Print the GCD
print("The GCD of", num1, "and", num2, "is", gcd)
