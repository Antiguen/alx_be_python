# Define the fixed interest rate (5% as a decimal)
ANNUAL_INTEREST_RATE = 0.05
MONTHS_PER_YEAR = 12

# 1. User Input for Financial Details
income_input = input("Enter your monthly income: ")
expenses_input = input("Enter your total monthly expenses: ")

# Convert inputs to float for calculation (to handle potential cents/decimals)
try:
    monthly_income = float(income_input)
    monthly_expenses = float(expenses_input)
except ValueError:
    print("Invalid input. Please enter valid numbers for income and expenses.")
    # Exit or set values to 0 to prevent further errors
    monthly_income = 0.0
    monthly_expenses = 0.0

# 2. Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# 3. Project Annual Savings
annual_savings_base = monthly_savings * MONTHS_PER_YEAR
interest_earned = annual_savings_base * ANNUAL_INTEREST_RATE

# Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_savings = annual_savings_base + interest_earned

# 4. Output Results
# Display monthly savings
# Ensure output matches example formatting exactly, using one decimal place for currency
print(f"Your monthly savings are ${monthly_savings:.0f}.") 

# Display projected annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
