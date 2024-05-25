import requests
from getpass import getpass

URL = 'https://httpbin.org/basic-auth/sebsx/0311'

password = getpass('Ingresa la contraseña: ')

session = requests.Session()
session.auth = ('sebsx', password)  # (user, password)

response = session.get(URL)

if response.status_code == 200:
    print(response.json())
else:
    print('Contraseña incorrecta. Acceso denegado.')
