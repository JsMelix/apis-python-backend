import requests

# GET = get 
# POST = post 
# PUT = put 
# DELETE = delete 


URL = 'https://httpbin.org/put'
response = requests.put(URL, 
                        params={'name': 'sebasx'},
                         headers={'version': '2.0'},
                         data={'id': 1})

if response.status_code == 200:
    print(response.text)