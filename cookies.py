import requests

URL = 'https://httpbin.org/cookies'

cookies = {
    'sessions': 'abc123',
    'name': 'sebxsia03@.com'
}

response = requests.get(URL, cookies=cookies)

if response.status_code == 200: 
    print(response.json())