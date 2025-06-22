# Simple Python Calculator
# Author: Manobika Sarkar
# Description: A basic calculator that performs addition, subtraction,
# multiplication, and division based on user input.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Check for division by zero
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Display options to the user
print("Welcome to the Python Calculator!")
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input
choice = input("Enter choice (1/2/3/4): ")

# Take input numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()

# Perform the selected operation
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice! Please select a valid option.")
