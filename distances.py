import numpy as np

def eucledianDist(x, y):
  euc = 0
  for i in range(len(x)):
    euc += (y[i] - x[i]) ** 2
  return np.sqrt(euc)
