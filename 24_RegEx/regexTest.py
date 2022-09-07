# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string


import re

txt = """
    I am Vikram. I have completed B.E Computer Science and Engineering. Now i am 
    I am Sarun. I have completed B.tech Computer Science and Engineering. Now i am 
    I am Duce. I have completed Masters of Computer Science and Engineering. Now i am 
    I am Harry. I have completed B.E Computer Science and Engineering. Now i am 
    I am Zayn. I have completed MBA 
    and Engineering. Now i am 
    I am Aron. I have completed B.E Computer Science 
    and Engineering. Now i am 
    I am Luke. I have completed B.Sc 
"""

x = re.search("(?<=I am ).*(?=.I)",txt)
print(x)

x = re.findall("(?<=I am ).*(?=. I)",txt)
print(x)

for i in x:
    if i == "Harry":
        print("Harry is presented in the string")


x = re.split("(?<=I am ).*(?=. I)",txt)
print(x)

x = re.sub("(?<=I am ).*(?=. I)","Duceman",txt)
print(x)