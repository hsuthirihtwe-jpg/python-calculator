# Basic Calculator

while True:
    print("\nSimple Calculator")
    print("Enter 'quit' to exit")
    
    num1 = input("Enter first number: ")
    if num1.lower() == 'quit':
        break
    num2 = input("Enter second number: ")
    if num2.lower() == 'quit':
        break
    operator = input("Enter operator (+, -, *, /): ")
    if operator.lower() == 'quit':
        break
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Invalid operator")
            continue
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers")
