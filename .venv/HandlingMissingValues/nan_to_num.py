#np.nan_to_num(array, num=value) default value is -0-

import numpy as np
arr = np.array([1,3,np.nan,5,np.nan,10])
cleaned_arr = np.nan_to_num(arr,nan=84)
print(cleaned_arr)
# print(np.isnan(arr))