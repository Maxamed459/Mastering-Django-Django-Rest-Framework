import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth"

username = input("Enter your username\n")
password = getpass("Enter your password\n")

auth_response_data = requests.post(auth_endpoint, json={'username': username, 'password': password})
# print(auth_response_data.json())

if auth_response_data.status_code == 200:
    token = auth_response_data.json()['token']
    # print(token)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/books"
    response_data = requests.get(endpoint, headers=headers)
    # print(response_data.json())
    data = response_data.json()
    print(data)
    print("here is the other requests")
    next_url = data['next']
    if next_url is not None:
        response_data = requests.get(next_url, headers=headers)
        print(data)


# print(auth_response_data.status_code)

# print(response_data.status_code)
# datas = response_data.json()
# for data in datas:
#      print(
#         f"The title of the book is {data['title']} and the author is {data['author']}, "
#         f"the ISBN is {data['ISBN']}, the price is {data['price']}, "
#         f"you got {data['discount']} off and you will pay {data['sale_price']}."
#     )

# print(response_data.status_code)