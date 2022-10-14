import re


text = "Hello My Name is Vikram." \
       "Hello My Name is Sarun."

searchTest = re.Search("(?<=Hello My Name is ).*(?=\.)",text)
print(searchTest)