import numpy as np
arr = np.array([3,54,np.inf,232,-np.inf,98])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr,posinf=1000, neginf=-100)
print(cleaned_arr)