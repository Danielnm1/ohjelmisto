# def is_prime(number):
#     if number<2:
#         return False
#     else:
#         isprime = True
#     for n in range(2,number):
#         if number%n==0:
#             isprime= False
#             break
#     return isprime
# import requests
#
# keyword = input("Enter keyword: ")
# request_url = "https://api.tvmaze.com/search/shows?q=" + keyword
# response = requests.get(request_url).json()  # convert JSON response to Python data
# print(response)
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
print(response)

