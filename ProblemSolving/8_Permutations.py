
# A Python program to print all
# permutations using library function
from itertools import permutations


# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3, 4])

# Print the obtained permutations
for i in list(perm):
    print (i)


def generate_permutations(elements):

    n = len(elements)

    c = [0] * n

    result = []

    result.append(elements[:])

    i = 0

    while i < n:

        if c[i] < i:

            if i % 2 == 0:

                elements[0], elements[i] = elements[i], elements[0]

            else:

                elements[c[i]], elements[i] = elements[i], elements[c[i]]

            result.append(elements[:])

            c[i] += 1

            i = 0

        else:

            c[i] = 0

            i += 1

    return result

elements = [1, 2, 3]

permutations = generate_permutations(elements)

print(permutations)

list1 = [1, 2, 3]