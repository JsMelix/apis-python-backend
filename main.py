import requests 

URL = 'https://httpbin.org/get'

response = requests.get(URL) # GET 
print (response)
print (response.status_code)
print (response.text) # str 
print(type(response.text)) 
print(response.json()) # dict 
payload = response.json()
print(payload. get ('origin')) 

print(response.url) 