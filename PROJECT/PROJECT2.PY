# Simple Calculator in Python

def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Get user input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get the operation choice
    choice = input("Enter the operation (+, -, *, /): ")
    
    # Perform calculation based on choice
    if choice == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice!")

# Run the calculator
calculator()
