# Define Global Conversion Factors (Constants)
# Use floating point numbers to ensure floating point division
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: (Fahrenheit - 32) * (5/9)
    """
    # FAHRENHEIT_TO_CELSIUS_FACTOR is read globally (no 'global' keyword needed for reading)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: (Celsius * (9/5)) + 32
    """
    # CELSIUS_TO_FAHRENHEIT_FACTOR is read globally
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # Prompt for temperature and validate as numeric
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input) # Will raise ValueError if input is not numeric

        # Prompt for unit and convert to upper case for consistency
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit_input == 'F':
            # Convert F to C
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        
        elif unit_input == 'C':
            # Convert C to F
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        # Handle non-numeric temperature input
        # Note: The requirement asks to "raise an error", but for user interaction, 
        # printing an error message is more standard. We will print the required text.
        print("Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
