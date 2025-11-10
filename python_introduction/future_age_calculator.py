# Define the number of years between the assumed current year (2023) and the future year (2050)
YEARS_TO_ADD = 27

# 1. Prompt the user for their current age.
age_input = input("How old are you? ")

# 2. Convert the input to an integer and calculate the future age.
# We rely on the assumption that the user inputs a valid integer.
current_age = int(age_input)
future_age = current_age + YEARS_TO_ADD

# 3. Print the result in the specified format: "In 2050, you will be [age] years old."
print(f"In 2050, you will be {future_age} years old.")
