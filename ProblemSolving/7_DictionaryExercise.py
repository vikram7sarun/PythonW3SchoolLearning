# Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Solution 1

res_dict = dict(zip(keys, values))
print(res_dict)

# Solution 2

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

# ----------------------------------------------------

# Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# ---------------------------------------------------

# Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# solution
print(sampleDict['class']['student']['name'])
print(sampleDict['class']['student']['marks']['history'])

# ----------------------------------------------------
'''



'''