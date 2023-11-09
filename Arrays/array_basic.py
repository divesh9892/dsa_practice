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

def arrayAppend(value):
    arr1.append(value)
    return arr1
print(arrayAppend(20))

def arrayExtend(value): 
    arr1.extend(value)
    return arr1
print(arrayExtend(ar.array('i', [32,23,65,78])))

def arrayFromList(value):
    arr1.fromlist(value)
    return arr1
print(arrayFromList([88,66,55,44]))


# deletion in array
def arrayDelete(value):
    arr1.remove(value)
    return arr1
print(arrayDelete(9))

def arrayPop():
    arr1.pop()
    return arr1
print(arrayPop())

# reversing an array
arr1.reverse()
print(arr1)

#getting array buffer information of given array
print(arr1.buffer_info())

#counting number of occurences of an element in given array
arr1.append(2)
print(arr1.count(2))

#converting array to list
print(arr1.tolist())

#slicing of an array
print(arr1[1:4])
print(arr1[1:])
print(arr1[:])
print(arr1[:-1])