# Create a string made of the first, middle and last character

str1 = "Jagan"

# Get first character
res = str1[0]

# Get string size
l = len(str1)

# Get middle index number
mi = int(l / 2)

# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)


# -------------------------------------------------------------------------------

# Create a string made of the middle three characters
def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)


get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")


# -------------------------------------------------------------------------------

# Create a new string made of the first, middle, and last characters of each input string

def mix_string(s1, s2):
    # get first character from both string
    first_char = s1[0] + s2[0]

    # get middle character from both string
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_char + middle_char + last_char
    print("Mix String is ", res)


s1 = "Argentina"
s2 = "Belgium"
mix_string(s1, s2)


# -----------------------------------------------------------

# Count all letters, digits, and special symbols from a given string

def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)


sample_str = "S@yn243hg&$$^&at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(sample_str)

# -----------------------------------------------------------

# Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)


s1 = "Bangalore"
s2 = "Delhi"


fl = s1[0]
f2 = s2[0]

ll = s1[-1]
l2 = s2[-1]

m1 = s1//2
m2 = 32//2

print()



# ---------------------
























