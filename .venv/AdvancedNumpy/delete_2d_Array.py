import numpy as np

arr_2d = np.array([[23,55,54,34],[34,65,98,30]])
print(arr_2d)
new_arr_2d = np.delete(arr_2d, 0 ,axis=0)
new_arr1_2d = np.delete(arr_2d, 0 ,axis=1)

print(new_arr_2d)
print(new_arr1_2d)