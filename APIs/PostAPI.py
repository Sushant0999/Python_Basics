import requests


def data():
    posts = requests.post("https://jsonplaceholder.typicode.com/posts/")
    print(posts.json())


data()

