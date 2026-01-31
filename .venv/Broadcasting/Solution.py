import numpy as np

prices = np.array([1000,500,300])
discount = 14
final_prices = prices-(prices * discount/100)
print(final_prices)