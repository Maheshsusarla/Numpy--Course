
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.median(a))
print(np.mod(a))
print(np.ar(a))

matrixs
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
r=arr1@arr2
p=arr1*arr2
print(r)
print(p)



# BeginnerTask 1
# Import NumPy and create a 1D array with the numbers 5, 10, 15, 20, 25. Print the array and its data type.
# Hint: use np.array() and .dtypek done
import numpy as np
# arr=np.array([5,10,15,20,25])
# print(arr)
# print(arr.dtype)
# BeginnerTask 2
# Create a 3×3 matrix of all zeros, then a 3×3 matrix of all ones. Print both.
# Hint: use np.zeros() and np.ones() with a tuple for shape
# arr=np.zeros((3,3))
# arr1=np.ones((3,3))
# print(arr)
# print(arr1)
# BeginnerTask 3
# Create an array of integers from 1 to 20 (inclusive) using a single NumPy function.
# Hint: np.arange(start, stop+1)
# arr=np.arange(1,21)
# print(arr)
# BeginnerTask 4
# From the array [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], extract the first 3 elements, the last 3 elements, and the element at index 5.
# arr=np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print(arr[0:3])
# print(arr[-3:])
# print(arr[5])
# BeginnerTask 5
# Find the shape, number of dimensions, total size, and data type of this array: [[1,2,3],[4,5,6],[7,8,9]]
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a.shape)
# print(a.ndim)
# print(a.size)
# print(a.dtype)
# # BeginnerTask 6
# # Add 100 to every element of the array [5, 10, 15, 20] without using a loop.ne
# a=np.array([5, 10, 15, 20])
# a+=100
# print(a)
# # BeginnerTask 7
# # Create a 4×5 array filled with the value 7 using a single NumPy function.
# # Hint: np.full(shape, value)
# a=np.full((4,5),7)
# print(a)
# # BeginnerTask 8
# # From the 2D array below, extract: (a) the entire second row, (b) the entire third column.
# # [[10,20,30],[40,50,60],[70,80,90]]
# a=np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(a[1:,])
# print(a[:,2])
# # BeginnerTask 9
# # Find the sum, mean, minimum, and maximum of the array [3, 7, 2, 9, 5, 1, 8, 4, 6].
# a=np.array([3, 7, 2, 9, 5, 1, 8, 4, 6])
# print(a.sum())
# print(a.mean())
# print(a.min())
# print(a.max())
# # BeginnerTask 10
# # Sort the array [42, 7, 19, 3, 55, 28] in ascending order, then find the index of the largest element in the original array.
# a=np.array([42, 7, 19, 3, 55, 28] )
# a.sort()
# print(a)
# IntermediateTask 11
# Reshape a 1D array of numbers 1–24 into a 3D array of shape (2, 3, 4). Print the shape to verify.
# Hint: total elements must match: 2×3×4 = 24
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
# b=a.reshape(2,3,4)
# print(b)
