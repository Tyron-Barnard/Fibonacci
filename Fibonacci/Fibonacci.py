# Define a function to calculate the Fibonacci sequence
def fibonacci_sequence(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_sequence(n - 2) + fibonacci_sequence(n - 1)

# Get input from the user
number = int(input("Enter a positive integer: "))

# Check if the input is valid
if number < 0:
    print("Invalid number")
else:
    print("Fibonacci sequence:")
    
    # Print the Fibonacci sequence up to the entered number
    for i in range(0, number):
        print(fibonacci_sequence(i))
