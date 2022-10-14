str = "ababcdsafaabbfff"
str = str.replace(" ","")

dict = {}

print(str.count("f"))

for i in str:
    if i in dict:
        dict[i] = dict.get(i)+1
    else:
        dict[i] = 1

print(dict)