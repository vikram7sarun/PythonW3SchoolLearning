def my_function():
    """
    Normal Function
    :return:
    """
    print("Hello from a function")
my_function()
# -----------------------------------------------
def my_function(fname):
    """
    # Function with one argument
    :param fname:
    :return None:
    """
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# -----------------------------------------------

def my_function(fname, lname):
    """
    # Function with two argument
    :param fname:
    :param lname:
    :return:
    """
    print(fname + " " + lname)


my_function("Sarun", "Vikram")


# -----------------------------------------------

# Arbitrary Arguments, *args

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# -----------------------------------------------

def my_function(child3, child2, child1):
    """
    # Keyword Arguments - assigning the names when calling the function
    :param child3:
    :param child2:
    :param child1:
    :return:
    """
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# -----------------------------------------------

"""
# Arbitrary Keyword Arguments, 
  **kwargs If you do not know how many keyword arguments that will be passed into your 
# function, add two asterisk: 
  ** before the parameter name in the function definition
# It will be stored in Dictionary we can use kid["lname"] to fetch data or loop
"""

def my_function(**kid):
    print("His last name is " +kid["lname"])


my_function(fname="Tobias", lname="Vikram")

# -----------------------------------------------
# Default Parameter Value

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# -----------------------------------------------


# Passing a List as an Argument

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

# Recursion
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
# def greet():
#     print("hello")
#     greet()
#
# greet()
