import requests

endpoint = "https://jsonplaceholder.typicode.com/users"
endpoint = "http://localhost:8000/api/"

response_data = requests.get(endpoint)

print(response_data.json()['message'])
# print(response_data.status_code)