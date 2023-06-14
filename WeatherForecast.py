import requests

class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"Weather forecast for {city}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature} K")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Unable to retrieve weather information.")

def main():
    api_key = "YOUR_API_KEY"
    city = "London"

    forecast = WeatherForecast(api_key)
    forecast.get_weather(city)

if __name__ == "__main__":
    main()
