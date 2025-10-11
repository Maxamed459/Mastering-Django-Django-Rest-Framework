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
    

response_data = requests.post(endpoint, json=data)

# print(response_data.status_code)
print(response_data.json())
# print(response_data.status_code)