
from typing import Any
#---------------------------Unpacking-------------------------------
#unpacking tuple
fname, lname = ("Sarun","Vikram")
print(fname)
print(lname)

#unpacking list
first , *rest = ["duce","zayn","harry","Aroon"]
print(first)
print(rest)

#unpacking Dictionary

specs = {"type":"dynamic","optional":"Static typing","found":"Everywhere"}
lang = {"Name":"Vikram",**specs}

print(specs)
print(lang)

#-----------------------------Variable Arguments -------------------------------------

def unknown_Friends(*args: str) -> None:
    for friend in args:
        print(friend)

unknown_Friends("sarun","Vikram","Duce","Aroon")

#-----------------------------Keyword Arguments --------------------------------------

def unknown_product(**kwargs: Any) -> None:
    for k,v in kwargs.items():
        print(f"{k}: {v}")

unknown_product(name="Pizza",price=3.99, topping="Olives", extra_chees=True)

#------------------------------Compbine args and kwargs------------------------------

def invoice(product: str, *args, **kwargs) -> None:
    print(product)
    print(args)
    print(kwargs)

invoice("Sneakers","black","white",brand="Nike",category="Air Jordans", price=899.99, insock=False)














