"""
Variable Scope:
------------------
Scope can be 'Global' or 'Local'
"""

num = 10

def print_global_num():
    print(f"Global num is : {num}")

def print_num():
    num = 20       #variable Shadowing - function or local scope
    print(f"Local num is : {num}")

def inc_num():
    global num  # Explicit Global Declaration
    num += 2

def inc_local_num():
    new_num = num + 10
    print(new_num)

print_global_num()
print_num()
inc_num()
inc_local_num()
print(num)