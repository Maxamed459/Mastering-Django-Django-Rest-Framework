import requests

endpoint = "http://localhost:8000/api/books/8/"

response_data = requests.get(endpoint)
print(response_data.json())