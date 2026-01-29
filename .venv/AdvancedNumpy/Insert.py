"""

np.insert(array, index,value,asix=none)
array-original array
index -
value-
axis-
axis=0, row-wise
1 means column wise
"""
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
new_arr = np.insert(arr, 2, 100)
new1_arr = np.insert(arr ,5,1000)
print(new_arr,new1_arr)