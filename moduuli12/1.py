import requests

# URL to get a random Chuck Norris joke
url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)
    if response.status_code == 200:
        # Convert response to JSON
        joke_data = response.json()
        # Print only the joke text
        print(joke_data["value"])
    else:
        print(f"Failed to fetch joke. Status code: {response.status_code}")
except requests.exceptions.RequestException:
    print("Could not connect to the Chuck Norris joke service.")
