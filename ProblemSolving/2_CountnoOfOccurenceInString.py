str = "S@yn243sh4g5&$$^&@@at&#i5vaae"
str = str.replace(" ","")

dict = {}

print(str.count("f"))

for i in str:
    if i in dict:
        dict[i] = dict.get(i)+1
    else:
        dict[i] = 1

print(dict)

#---------------------------------------------------

Str1 = "S@yn243sh4g5&$$^&@@at&#i5vaae"

str_d = {}

for i in Str1:
    val = Str1.count(i)
    str_d[i] = val
print(str_d)