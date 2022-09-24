
# Normal Function

def add_Num(num):
    num = num+10
    print(num)

add_Num(10)

# lambda Function   -> anonymous function

add_num = lambda x:x+10
print(add_num(10))

product = lambda a,b,c:a*b*c
print(product(2,4,6))

tall_enough = lambda h:h>175
print(tall_enough(176))

strong_enough = lambda w: "YES" if w>100 else "NO"
print(strong_enough(20))



