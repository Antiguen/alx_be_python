def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations (add, subtract, multiply, divide).
    Returns the result or an error message string for division by zero.
    """
    op = operation.strip().lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 == 0:
            # EXACT STRING REQUIRED
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'."
