def calculator():
    """
    A simple calculator that uses the match-case statement to perform
    addition, subtraction, multiplication, and division.
    It handles input validation and division by zero.
    """
    try:
        # Prompt for user input, casting to float to handle decimals
        num1_input = input("Enter the first number: ")
        num1 = float(num1_input)
        
        num2_input = input("Enter the second number: ")
        num2 = float(num2_input)
        
        operation = input("Choose the operation (+, -, *, /): ").strip()
        
    except ValueError:
        # Handle cases where the input numbers are not valid floats
        print("Invalid input. Please enter valid numeric values for both numbers.")
        return

    result = None
    message = ""

    # Perform the calculation using the match case statement
    match operation:
        case '+':
            result = num1 + num2
            message = f"The result is {result}."
        
        case '-':
            result = num1 - num2
            message = f"The result is {result}."
            
        case '*':
            result = num1 * num2
            message = f"The result is {result}."
            
        case '/':
            # Handle division by zero case
            if num2 == 0:
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

