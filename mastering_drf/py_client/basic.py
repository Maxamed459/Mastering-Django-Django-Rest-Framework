import requests

# endpoint = "https://jsonplaceholder.typicode.com/users"
endpoint = "http://localhost:8000/api/books/"

data = {
        "id": 3,
        "title": "Django REST Framework in Action",
        "author": "Maxamed Mahdi",
    }
    # {
    #     "title": "Rich Dad and Boor Dad",
    #     "author": "Rich Dad",
    #     "ISBN": "12345",
    #     "price": 12.99
    # },
    
headers = {
    "Authorization": f"Bearer 3e58eee350c07c62043c745166a9cb6d3ce839af"
}

response_data = requests.post(endpoint, json=data, headers=headers)

# print(response_data.status_code)
print(response_data.json())
# print(response_data.status_code)