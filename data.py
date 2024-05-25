import requests

URL = 'https://httpbin.org/post'

data = {
     'username': 'eduardo' ,
     'password': 'password123',
}

response = requests. post (URL, data=data)

if response.status_code == 200:
     payload = response. json ( )
     print(response.text)

     print(response.url)