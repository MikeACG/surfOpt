import random as rd

def realInd(lls, uls):
  return [rd.uniform(lls[g], uls[g]) for g in range(len(lls))]