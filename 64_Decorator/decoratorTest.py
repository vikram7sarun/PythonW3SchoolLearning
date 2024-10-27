# Decorator  = A function that extends the behaviour of the function w/0 modifying the base function
# pass  the base function as an arguments to the decorator


def add_sprinkles(func):
    def wrapper():
        print("You add sprinkles")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("You add fudge")
        func()
    return wrapper
@add_sprinkles
@add_fudge
def get_ice_cream():
    print("Here is your ice cream")

get_ice_cream()