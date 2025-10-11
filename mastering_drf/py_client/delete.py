import requests


book_id = input("Enter the book id you want to delete? \n")
try:
    book_id = int(book_id)
except: 
    book_id = None
    print("invalid id")

if book_id is not None:
    endpoint = f"http://localhost:8000/api/books/{book_id}/delete"


    response_data = requests.delete(endpoint)
    print(response_data.status_code, response_data.status_code == 204)