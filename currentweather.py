import requests

def get_weather_data():
    # URL for the Open-Meteo API with specified latitude and longitude
    url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current_weather=true"

    try:
        # Make a request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request was unsuccessful

        # Parse the JSON response
        data = response.json()

        # Extract the current temperature and wind direction
        current_temperature = data['current_weather']['temperature']
        wind_direction = data['current_weather']['winddirection']

        # Print the current temperature and wind direction
        print(f"Current Temperature: {current_temperature}°C")
        print(f"Wind Direction: {wind_direction}°")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    get_weather_data()
