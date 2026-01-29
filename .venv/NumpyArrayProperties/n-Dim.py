import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[4,5,6],[90,45,23]])
arr_3d = np.array([[[7,8,9],
                    [10,11,12],
                    [13,14,15]]])
print(arr_1d.ndim, arr_2d.ndim, arr_3d.ndim)