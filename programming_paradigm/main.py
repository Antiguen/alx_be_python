# main.py

import sys
# Import the safe_divide function from the robust_division_calculator module
from robust_division_calculator import safe_divide

def main():
    # Check if the correct number of arguments (script name + numerator + denominator) are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Arguments are passed as strings from the command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # The safe_divide function handles all conversion and error logic
    result = safe_divide(numerator, denominator)
    
    # Print the result or the error message returned by the function
    print(result)

if __name__ == "__main__":
    main()