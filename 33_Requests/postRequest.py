import requests

request_payload = {
                  "name": "morpheus",
                  "job": "leader"
                  }
url = "https://reqres.in/api/users"
param={}
# headers = {'user-agent': 'my-app/0.0.1'}
# files= files
# cookies = dict(cookies_are='working')
# basic = HTTPBasicAuth('user', 'pass')    #Basic Authentication  --  auth=basic
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET','USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# class MyAuth(requests.auth.AuthBase):
# ...     def __call__(self, r):
# ...         # Implement my authentication
# ...         return r
# ...
# >>> url = 'https://httpbin.org/get'
# >>> requests.get(url, auth=MyAuth())




r = requests.post(url, data=request_payload)
print(r.json())

# print(r.cookies['example_cookie_name'])


id = r.json()
print("Id : "+id['id'])

