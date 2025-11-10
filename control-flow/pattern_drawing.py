# 1. Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# 2. Draw the Pattern using nested loops

row_counter = 0

# The WHILE loop iterates through each row
while row_counter < size:
    
    # The FOR loop iterates through each column in the current row (Inner loop)
    for column_counter in range(size):
        # Print the asterisk without a newline
        print("*", end="")
    
    # Print a newline character after the row is complete
    print() 
    
    # Increment the row counter
    row_counter += 1
