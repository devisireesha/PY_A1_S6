# To print the fibonacci series using recursive method

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Take input from user
n = int(input("Enter the number of terms:"))
# Print the Fibonacci series using recursive method
if n <= 0:
    print("Invalid input!")
else:
    print("Fibonacci series:")
    for i in range(n):
        print(fibonacci_recursive(i), end=' ')
