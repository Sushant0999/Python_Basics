import requests


def data():
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    print(users.json())


data()
