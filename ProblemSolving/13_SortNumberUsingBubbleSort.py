
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


