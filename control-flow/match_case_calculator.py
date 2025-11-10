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
        # Convert to float
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        # Gracefully handle non-numeric input
        return # Simply exit if input is bad, as it wasn't the primary task requirement

    # Perform the calculation using the match case statement
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
            
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
            
        case '/':
            # CRITICAL: Handle division by zero case
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
                
        case _:
            # Default case for invalid operation input
            print(f"Invalid operation '{operation}'. Please choose one of (+, -, *, /).")

if __name__ == "__main__":
    calculator()

