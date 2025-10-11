import requests

endpoint = "http://localhost:8000/api/books/8/update"

# on patch
# data = {
#     # only the field you want to update
#     "title": "The Rich Dad and Boor Dad"
# }

# on put you will give it all the required fields
data = {
    'title': 'The Rich Dad and Boor Dad', # required
    'author': 'Rich Dad', # required
    'ISBN': '12345',
    'price': '12.99'
}

response_data = requests.put(endpoint, json=data)
print(response_data.json())