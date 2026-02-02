#np.isinf(array) 30,10^10000,
# 1/0
import numpy as np
arr = np.array([3,54,np.inf,232,-np.inf,98])
print(np.isinf(arr))