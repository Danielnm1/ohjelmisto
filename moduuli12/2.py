import requests

city = input("Enter the name of a municipality: ")
api_key = "a4c2e461f8c9f6534e1520a88f7efca7"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temp_celsius = data["main"]["temp"]

        print(f"Weather in {city}: {description}")
        print(f"Temperature: {temp_celsius:.2f}°C")
    else:
        print(f"Could not fetch weather data. Status code: {response.status_code}")
except requests.exceptions.RequestException:
    print("Failed to connect to the OpenWeather API.")

