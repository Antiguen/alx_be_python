while True:
    try:
        # Prompt user and save in variable 'number'
        number_input = input("Enter a number to see its multiplication table: ")
        # Using int() here handles the requirement for multiplication table calculation
        number = int(number_input) 
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# 2. Generate and Print the Multiplication Table (from 1 to 10)
# range(1, 11) generates numbers 1, 2, 3, ..., 10
for i in range(1, 11):
    # Calculate the product
    product = number * i
    
    # CRITICAL FIX: Print each line in the required format: "X * Y = Z"
    # Using simple concatenation/format to guarantee the exact output string.
    print(f"{number} * {i} = {product}")

