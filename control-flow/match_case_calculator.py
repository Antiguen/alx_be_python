def calculator():
    try:
        num1_input = input("Enter the first number: ")
        num1 = float(num1_input)
        
        num2_input = input("Enter the second number: ")
        num2 = float(num2_input)
        
        operation = input("Choose the operation (+, -, *, /): ").strip()
        
    except ValueError:
        # NOTE: The task only asked to raise an error for invalid temperature, 
        # but for a cleaner UX, we handle non-numeric input here.
        print("Invalid input. Please enter valid numeric values for both numbers.")
        return

    result = None
    message = "" # Initialize message string

    match operation:
        case '+':
            result = num1 + num2
            # CRITICAL: Must be EXACTLY "The result is [result]."
            message = f"The result is {result}."
        
        case '-':
            result = num1 - num2
            message = f"The result is {result}."
            
        case '*':
            result = num1 * num2
            message = f"The result is {result}."
            
        case '/':
            if num2 == 0:
                # CRITICAL: Must be EXACTLY "Cannot divide by zero."
                message = "Cannot divide by zero."
            else:
                result = num1 / num2
                message = f"The result is {result}."
                
        case _:
            message = f"Invalid operation '{operation}'. Please choose one of (+, -, *, /)."

    # Output the result or error message
    print(message)

if __name__ == "__main__":
    calculator()
