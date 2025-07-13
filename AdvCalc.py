## Day 1
def calculator():
    print("Welcome to the Calculator!")
    print("-" * 30)
    
    # Get the first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a valid number!")
    
    # Get the second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Please enter a valid number!")
    
    # Show operation options
    print("\nWhat operation would you like to perform?")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    # Get operation choice
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in range(1, 5):
                break
            else:
                print("Please enter a number between 1 and 4!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Perform the calculation
    if choice == 1:
        result = num1 + num2
        operation = "+"
    elif choice == 2:
        result = num1 - num2
        operation = "-"
    elif choice == 3:
        result = num1 * num2
        operation = "*"
    elif choice == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2
        operation = "/"
    
    # Display the result
    print(f"\n{num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()