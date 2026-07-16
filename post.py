import requests

new_todo = {
    "userId": 1,
    "title": "Learn Requests",
    "completed": False
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data =new_todo)
response.raise_for_status()

print(response.text)