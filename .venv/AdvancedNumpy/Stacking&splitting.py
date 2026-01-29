"""
vertically
horizontally

vstack() row wise
hstack() column wise
"""

import numpy as np

arr1 = np.array([3,4,5])
arr2 = np.array([9,2,1])

print(np.hstack((arr1,arr2)))
print(np.vstack((arr1, arr2)))