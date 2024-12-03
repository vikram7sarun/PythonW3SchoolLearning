def iterative_permutations(string):
    # Start with a single empty permutation
    result = [""]

    for char in string:  # Loop through each character in the string
        new_result = []  # Store new permutations
        for perm in result:  # Loop through each existing permutation
            for i in range(len(perm) + 1):  # Insert the current character at every position
                new_result.append(perm[:i] + char + perm[i:])
        result = new_result  # Update the result with new permutations

    return result


# Input string
string = "abc"
permutations = iterative_permutations(string)
print(permutations)
