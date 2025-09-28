def provide_weather_advice():
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    if weather == 'sunny':
        recommendation = "Wear a t-shirt and sunglasses."
    elif weather == 'rainy':
        recommendation = "Don't forget your umbrella and a raincoat."
    elif weather == 'cold':
        recommendation = "Make sure to wear a warm coat and a scarf."
    else:
        recommendation = "Sorry, I don't have recommendations for this weather."

    print(recommendation)

if __name__ == "__main__":
    provide_weather_advice()
