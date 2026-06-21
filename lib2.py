
# IntermediateTask 11
# Reshape a 1D array of numbers 1–24 into a 3D array of shape (2, 3, 4). Print the shape to verify.
# Hint: total elements must match: 2×3×4 = 24
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
# b=a.reshape(2,3,4)
# print(b)
# IntermediateTask 12
# From the array [12, 5, 33, 7, 22, 41, 9, 18], extract only the elements that are greater than 15 using boolean indexing.
# Show answerAsk Claude ↗Mark done
# arr=np.array([12,5,33,7,22,41,9,18])
# res=arr[arr>15]
# print(res)
# IntermediateTask 13
# Given student marks: [45, 82, 58, 76, 91, 38, 65], use np.where() to label each as 'Pass' (>=60) or 'Fail'.
# arr=np.array([45, 82, 58, 76, 91, 38, 65])
# a=np.where(arr>=60,'pass','fail')
# print(a)

# IntermediateTask 14
# Stack these two arrays vertically (as rows) and horizontally (side by side):
# a = [1, 2, 3]   b = [4, 5, 6]
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(np.vstack([a,b]))
# print(np.hstack([a,b]))

# IntermediateTask 15
# For this 2D array, compute: (a) sum of each column, (b) mean of each row.
# [[4,8,2],[1,5,9],[7,3,6]]
# Hint: axis=0 means along columns, axis=1 means along rows
# a=np.array([[4,8,2],[1,5,9],[7,3,6]])
# print(a.sum(axis=0))
# print(a.mean(axis=1))

