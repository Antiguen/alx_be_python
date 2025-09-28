while True:
    try:
        size_input = input("Enter the size of the pattern: ")
        size = int(size_input)
        
        # Check if the number is a positive integer
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# 2. Draw the Pattern using nested loops

# Initialize row counter for the WHILE loop (Outer loop)
row_counter = 0

# The WHILE loop iterates through each row
while row_counter < size:
    
    # The FOR loop iterates through each column in the current row (Inner loop)
    # It prints 'size' number of asterisks side-by-side
    for column_counter in range(size):
        # The end="" prevents a newline, keeping the asterisks on the same line
        # Note: Using '*' * size is simpler, but the task explicitly requires a for loop here.
        print("*", end="")
    
    # After the FOR loop finishes printing the row, print a newline character
    print() # Prints a newline by default
    
    # Increment the row counter
    row_counter += 1

