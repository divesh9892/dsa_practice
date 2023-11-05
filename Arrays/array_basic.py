import array as ar

# creating an array
arr1 = ar.array('i', [1,2,3,4,5,6])
print(arr1)

# traversing an array
for x in arr1:
    print(x)

# get value from a specific index
def arrayIndex(index):
    if index>=len(arr1):
        return "No element present on the given index"
    return arr1[index]
print(arrayIndex(6))

# searching for a value
def arraySearch(value):
    for element in arr1:
        if element == value:
            return f"Value: {value} found on Index: {arr1.index(value)}"
    return "The given value does not exist in array"
print(arraySearch(1))

# insertion in array
def arrayInsert(index, value):
    arr1.insert(index, value)
    return arr1
print(arrayInsert(2,9))

# deletion in array
def arrayDelete(value):
    arr2 = ar.array('i', [1,2,2,3,2])
    arr2.remove(value)
    return arr2
print(arrayDelete(2))