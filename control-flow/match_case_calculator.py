def calculator():
    """
    A simple calculator that uses the match-case statement to perform
    addition, subtraction, multiplication, and division.
    It handles division by zero.
    """
    
    # Read inputs as strings first
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")
    operation = input("Choose the operation (+, -, *, /): ").strip()
    
    try:
        # Convert to float immediately before use in calculation
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        # Gracefully handle non-numeric input
        print("Invalid number input. Please enter numeric values.")
        return

    result = None
    message = ""

    # Perform the calculation using the match case statement
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
            # CRITICAL: Handle division by zero case
            if num2 == 0:
                # Must match task example exactly, including the period
                message = "Cannot divide by zero."
            else:
                result = num1 / num2
                message = f"The result is {result}."
                
        case _:
            # Default case for invalid operation input
            message = f"Invalid operation '{operation}'. Please choose one of (+, -, *, /)."

    # Output the result or error message
    print(message)

if __name__ == "__main__":
    calculator()
