
import requests

url = ""


x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

# Syntax
# requests.post(url, data={key: value}, json={key: value}, args)
# args means zero or more of the named arguments in the parameter table below. Example:
# requests.post(url, data = myobj, timeout=2.50)

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)