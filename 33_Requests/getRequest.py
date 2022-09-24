import requests

r = requests.get("https://reqres.in/api/users?page=2")
print(r.status_code)
print(r.headers)
print(r.headers['Content-Type'])
print(r.encoding)
print(r.text)
print(r.json())

emailList  = []
first_name = []


email = r.json()
print(email['data'][0]['email'])  # To Parse only single mail id with index

jlen = len(email['data'])  # To get the length of the Json object
print(type(jlen))
print(jlen)


#Fetch All email from the Json object

for i in range(0,jlen-1):
    m = email['data'][i]['email']
    emailList.append(m)

print(emailList)
