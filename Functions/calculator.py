'''Laura V. Bullock
10/17/2024
Week7 - Day2
Homework3-calculator.py

Write a calculator program.
Your code will provide 2 numbers and the user will select what type of operation needed.'''


# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for division
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return f"ERROR!!! \n\t{num1} can not be divided by {num2}. \n\tTherefore, will result in ZeroDivisionError: float division by zero"

# Function for modulus
def modulus(num1, num2):
    return num1 % num2

# Function for exponent
def exponent(num1, num2):
    return num1 ** num2

# Function to select the operation
def calculate():
    # Getting input from user
    num1 = float(input("\nPlease enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    # Display arithmetic operation options
    print("\nArithmetic operation options:\n\t")
    print("\t1. Add")
    print("\t2. Subtract")
    print("\t3. Multiply")
    print("\t4. Divide")
    print("\t5. Modulus")
    print("\t6. Exponent")

    # Input: Getting the operation selection
    selection = input("\nPlease enter the number (1,2,3,4,5,6) of your selection here:  ")

    # Perform calculation based on user's arithmetic operation selection
    if selection == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif selection == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif selection == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif selection == '4':
        result = divide(num1, num2)
        operation = "Division"
    elif selection == '5':
        result = modulus(num1, num2)
        operation = "Modulus"
    elif selection == '6':
        result = exponent(num1, num2)
        operation = "Exponent"
    else:
        return "Invalid input"

    return f"\n{operation} of {num1} and {num2} is: {result:0,.2f}" #2 decimal places in case division returns large decimal

print(f"{calculate()} \n\n\tThank you for playing.  Have a wonderfully blessed day!")
