def provide_weather_advice():
    """
    Prompts the user for weather conditions and provides clothing recommendations
    using if, elif, and else statements.
    """
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    if weather == 'sunny':
        # MUST MATCH EXACTLY
        recommendation = "Wear a t-shirt and sunglasses."
    elif weather == 'rainy':
        # MUST MATCH EXACTLY
        recommendation = "Don't forget your umbrella and a raincoat."
    elif weather == 'cold':
        # MUST MATCH EXACTLY
        recommendation = "Make sure to wear a warm coat and a scarf."
    else:
        # MUST MATCH EXACTLY
        recommendation = "Sorry, I don't have recommendations for this weather."

    print(recommendation)

if __name__ == "__main__":
    provide_weather_advice()
