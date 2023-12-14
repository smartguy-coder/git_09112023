import requests

urls = [f'https://dummyjson.com/users/{user_id}' for user_id in range(1, 50)]


for url in urls:
    response = requests.get(url)
    print(response)
