import numpy as np 
import numpy.typing as npt
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr)

# insertion in 2d array
arr = np.insert(arr, 0, [13,14,15,16], axis=0)
print(arr)
arr = np.insert(arr, 2, [13,14,15,16], axis=1)
print(arr)
arr = np.append(arr, [[55,44,33,22,11]], axis=0)
print(arr)

# accessing as element in 2d array
def access_elements(array: npt.NDArray, rowIndex: int, colIndex: int) -> str: 
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        return "Invalid index entered"
    return f"Value at array[{rowIndex}][{colIndex}]: {array[rowIndex][colIndex]}"

print(access_elements(arr, 1, 2))

# traversing 2d array
def traverse2d_arr(array):
    for x in range(len(array)):
        for y in range(len(array[0])):
            print(array[x][y])
traverse2d_arr(arr)

# linear search in 2d array
def two_d_array_search(array, value):
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == value:
                return f"Given value is located at index [{x}][{y}]"
    return "Value does not exist"
print(two_d_array_search(arr, 22))

#deletion in 2d array
print(np.delete(arr, 1, axis=0))
print(np.delete(arr, 2, axis=1))