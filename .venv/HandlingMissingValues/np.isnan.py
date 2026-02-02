#np.isnan(array)
import numpy as np
arr = np.array([1,2,np.nan,np.nan, 5, np.nan, 6,7])
print(np.isnan(arr))

#not
print(np.nan==np.nan)