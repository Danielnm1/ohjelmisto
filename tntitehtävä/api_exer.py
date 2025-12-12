import requests
keyword = input("enter the key word here: ")
response_url = "https://api.tvmaze.com/search/shows?q=" + keyword
try:
    response = requests.get(response_url)
    if requests.status_codes == 200:
        json_response = response.json()
        for show in json_response:
            print(show['show']['name'])
        else:
            print('Api error',requests.status_codes)
except requests.exceptions.RequestExceptions:
    print("request couldn't been completed")

