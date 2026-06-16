""" NumPy is used for fast numerical computations, array operations, matrix calculations, data analysis, 
machine learning, image processing, and scientific computing. 
it is much faster and more memory-efficient than Python lists.

Who Created NumPy:
NumPy was created by Travis Oliphant in 2005. It is an open-source library.

-> NumPy arrays are much faster than Python lists and use less memory.
-> NumPy stores data in contiguous memory locations. This allows the CPU to access nearby elements quickly.
"""
numpy
l=[1,2,3,4,5]
res=[]
for i in l:
    res.append(i+5)
print(res)

import numpy as np
arr=np.array([10,20,30])
print(arr+5)

np.zeros([1,2])
print(np.ones([1,3]))
a=np.random.rand(2,3)
a=np.random.randint(1,11)
a=np.arange(1,11)
a=np.array([[[1,2],[3,4],[5,6]]])
print(a.size)
print(a.shape)
print(a.ndim)
print(a[0][1][0])
print(np.__version__)
