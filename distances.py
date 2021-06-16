import numpy as np

# implements a simple eucledian distance between 2 vectors
def eucledianDist(x, y):
  euc = 0
  for i in range(len(x)):
    euc += (y[i] - x[i]) ** 2
  return np.sqrt(euc)
