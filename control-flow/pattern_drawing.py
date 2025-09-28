size = 0
try:
    # CRITICAL FIX: Removed .strip() and ensure exact prompt string
    size_input = input("Enter the size of the pattern: ")
    size = int(size_input)
except ValueError:
    # If input is not a number, size remains 0, drawing nothing.
    pass 

# 2. Draw the Pattern using nested loops

# Initialize row counter for the WHILE loop (Outer loop)
row_counter = 0

# The WHILE loop iterates through each row
while row_counter < size:
    
    # The FOR loop iterates through each column in the current row (Inner loop)
    for column_counter in range(size):
        # The end="" prevents a newline, keeping the asterisks on the same line
        print("*", end="")
    
    # After the FOR loop finishes printing the row, print a newline character
    print() 
    
    # Increment the row counter
    row_counter += 1

