from datetime import datetime, timedelta

def display_current_datetime():
    """
    Part 1: Gets and displays the current date and time in the specified format.
    """
    # Save the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    return current_date

def calculate_future_date(current_date):
    """
    Part 2: Prompts the user for a number of days and calculates the future date.
    
    Args:
        current_date (datetime): The starting datetime object.
    """
    while True:
        try:
            # Prompt the user for a number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer number of days.")

    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Execute Part 1: Display and store the current date
    current_dt = display_current_datetime()
    
    # Execute Part 2: Calculate the future date
    calculate_future_date(current_dt)

if __name__ == "__main__":
    main()
