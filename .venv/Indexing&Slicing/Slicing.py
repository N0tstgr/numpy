"""
slicing
array[start: stop:step]

arr[start:end], start to end -1
negative step -1 reverse
"""
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:6])
print(arr[:5])
print(arr[::3])
print(arr[::-1])