str = "ababcdsafaabbfff"
str = str.replace(" ","")

dict = {}


for i in str:
    if i in dict:
        count = dict.get(i)+1
        dict[i] = count
    else:
        dict[i] = 1

print(dict)



