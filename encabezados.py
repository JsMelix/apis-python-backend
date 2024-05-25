import requests

URL = 'https://httpbin.org/post'

# QUERY -> GET 
# Cuerpo de Petición -> POST 
# Encabezado -> all verbs 

headers = {
    'course': 'Curso de Python',
    'version': 'version 2.0',
    'author': 'sebsx',
}

params = {
    'platform': 'xeii courses'
}

data = {
    'username': 'Sebsx',
    'password': 'password123'
}


response = requests.post(URL, headers=headers, params=params, data=data)

if response.status_code == 200:
    print (response.text) 