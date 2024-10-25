
def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1 ):
            if(list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1

list1 = [6,3,8,9,7,2,4,1]
List2 = []
print("Before Sorting : ",list1)
list2 = bubble_sort(list1)
print("After Sorting : ", list2)



# Define the list
list1 = [6, 3, 8, 9, 7, 2, 4, 1,5]

len = len(list1)

# Implement Bubble Sort
for i in range(len - 1):
    for j in range(len - 1):
        if list1[j] > list1[j + 1]:
            # Swap if the current element is greater than the next element
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

# Print the sorted list
print("Sorted list:", list1)