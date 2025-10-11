import requests

endpoint = "http://localhost:8000/api/books"


response_data = requests.get(endpoint)

# print(response_data.status_code)
# datas = response_data.json()
# for data in datas:
#      print(
#         f"The title of the book is {data['title']} and the author is {data['author']}, "
#         f"the ISBN is {data['ISBN']}, the price is {data['price']}, "
#         f"you got {data['discount']} off and you will pay {data['sale_price']}."
#     )
print(response_data.json())
# print(response_data.status_code)