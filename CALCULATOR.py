def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def get_operation_choice():
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4) or 'exit' to quit: ")
    return choice

def calculator():
    print("Welcome to the Simple Calculator!")

    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    while True:
        choice = get_operation_choice()
        
        if choice.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            
            result = operations[choice](num1, num2)
            operation_symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
            print(f"{num1} {operation_symbols[choice]} {num2} = {result}")
        else:
            print("Invalid choice! Please choose a valid operation.")

if __name__ == "__main__":
    calculator()
