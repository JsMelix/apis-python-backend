import requests

URL = 'https://httpbin.org/get?name=sebas&password=wai031&email=sebsx03@gmail.com'
# query

response = requests.get(URL)

if response.status_code == 200:
     payload = response.json()
     params = payload[ 'args']

print(params ['name'])
print(params ['password'])
print(params ['email'])


