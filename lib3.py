
NumPy Array Reshaping : Reshaping means changing the shape (dimensions) of an array without changing its data.
The shape of an array tells how many elements are present in each dimension.
1d to 2d
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new=arr.reshape(4,3)
print(arr)
print(new)

1d to 3d
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new=arr.reshape(2,3,2)
print(arr)
print(new)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

Unknown Dimension : (-1)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12])
newarr = arr.reshape(2, 2, -1)
print(newarr)

array inerating
arr=np.array([1,2,3,4])
for x in arr:
    print(x)

arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
    print(x)
arr=np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
    for y in x:
        print(y)

arr = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
for x in arr:
    print(x)
arr = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
for x in arr:
   for y in x:
    for z in y:
        print(z)
