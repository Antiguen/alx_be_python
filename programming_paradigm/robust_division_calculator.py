# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division robustly, handling ZeroDivisionError and ValueError.

    Args:
        numerator (str): The numerator, passed as a string from command line.
        denominator (str): The denominator, passed as a string from command line.

    Returns:
        str: An error message or the result of the division.
    """
    try:
        # 1. Attempt to convert inputs to float (handles ValueError)
        num = float(numerator)
        den = float(denominator)

        # 2. Perform division (handles ZeroDivisionError)
        result = num / den
        
        # 3. Successful division
        return f"The result of the division is {result}"

    except ValueError:
        # Error for non-numeric input (e.g., 'ten' or '5a')
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Error for division by zero (denominator is 0)
        return "Error: Cannot divide by zero."

# Optional test block (not needed for main.py, but useful for debugging)
if __name__ == '__main__':
    print(safe_divide("10", "5"))
    print(safe_divide("10", "0"))
    print(safe_divide("ten", "5"))