def provide_weather_advice():
    """
    Prompts the user for weather conditions and provides clothing recommendations
    using if, elif, and else statements.
    """
    # 1. Prompt User for Weather Input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    # 2. Provide Clothing Recommendations
    if weather == 'sunny':
        recommendation = "Wear a t-shirt and sunglasses."
    elif weather == 'rainy':
        recommendation = "Don't forget your umbrella and a raincoat."
    elif weather == 'cold':
        recommendation = "Make sure to wear a warm coat and a scarf."
    else:
        # 3. Handle unexpected input with the else statement
        recommendation = "Sorry, I don't have recommendations for this weather."

    # 4. Output the Recommendation
    print(recommendation)

if __name__ == "__main__":
    provide_weather_advice()
