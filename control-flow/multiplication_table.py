while True:
    try:
        # Prompt user and save in variable 'number'
        number_input = input("Enter a number to see its multiplication table: ")
        number = float(number_input) # Use float to handle any numeric input, but calculation will be integer-based
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# 2. Generate and Print the Multiplication Table (from 1 to 10)
# range(1, 11) generates numbers 1, 2, 3, ..., 10
for i in range(1, 11):
    # Calculate the product
    product = number * i
    
    # Print each line in the required format: "X * Y = Z"
    # We use int(number) for cleaner output, but retain float logic above for robust input.
    print(f"{int(number)} * {i} = {int(product)}")
