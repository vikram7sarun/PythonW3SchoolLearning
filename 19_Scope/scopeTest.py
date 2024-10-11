def myfunc():
    x = 300
    print(x)


myfunc()


# Function Inside Function

def myfunc():
    x = 500

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

x = 300


def myfunc():
    print(x)


myfunc()

print(x)


def myfunc():
    global x
    x = 900


myfunc()

print(x)

# Closure is a function having access to the scope of its parent function after the parent function has returned.
