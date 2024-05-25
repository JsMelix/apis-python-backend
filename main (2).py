import requests

URL = 'https://httpbin.org/get'

params = {
     'name': 'sebas',
     'password': '1234',
     'email': 'sebs03@ai.com',
     }

response = requests.get(URL, params=params)

if response.status_code == 200:
     payload = response.json()
     params = payload[ 'args']

print(params ['name'])
print(params ['password'])
print(params ['email'])

print(response.url)
