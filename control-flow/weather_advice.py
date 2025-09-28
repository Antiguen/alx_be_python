def provide_weather_advice():
    # Final Fix Attempt: Simplify input processing and ensure no leading/trailing characters break the checker
    # Note: We must retain the EXACT prompt string.
    weather_input = input("What's the weather like today? (sunny/rainy/cold): ")
    weather = weather_input.strip().lower()

    # Provide Clothing Recommendations using direct print statements
    if weather == 'sunny':
        # Print MUST match EXACTLY
        print("Wear a t-shirt and sunglasses.")
    elif weather == 'rainy':
        # Print MUST match EXACTLY
        print("Don't forget your umbrella and a raincoat.")
    elif weather == 'cold':
        # Print MUST match EXACTLY
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # Handle unexpected input with the else statement
        # Print MUST match EXACTLY
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    provide_weather_advice()

