# Create a string made of the first, middle and last character

str1 = "Sarun"

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

#Create a new string made of the first, middle, and last characters of each input string

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

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)