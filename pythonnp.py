
# import numpy as np
# arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print(arr.ndim)

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# a=arr.reshape(2,8)
# print(a)

# e=np.empty((2,2))
# e[0,0]=1
# e[0,1]=2
# e[1,0]=3
# e[1,1]=4
# print(e)

# m=np.array([[1,2],[3,4]])
# flatten 
# print(m.flatten())
# n=m.flatten()
# m[0,0]=10
# print(m)
# print(n)

# ravel 
# n=m.ravel()
# m[0,0]=10
# print(m)
# print(n)

# transpose convert rows to cols and cols to rows
# print(m)
# print(m.transpose())

# stacks v-stack : vertical and h-stack -horizantal
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# c=np.array([7,8,9])
# print(np.vstack([a,b,c]))
# print(np.hstack([a,b,c]))

# concate similar hstack
# print(np.concatenate((a,b)))
# print(a++5)
# print(a*5)
# print(a==b)
# print(a++b)





import numpy as np
# check the data type
# a=np.array([1,2,3,4])
# print(a.dtype)
# arr = np.array([10.5,20.6,30.7])
# print(arr.dtype)
# arr = np.array(["Apple","Banana","Mango"])
# print(arr.dtype)
# arr = np.array([True,False,True])
# print(arr.dtype)

# Creating Array with Specific Data Type
# arr = np.array([1,2,3,4],dtype='S')
# print(arr)
# print(arr.dtype)

# copy 
# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)
# print(x.base)
#view
# arr = np.array([1,2,3,4,5])
# x = arr.view()
# x[0] = 31
# print(arr)
# print(x)
