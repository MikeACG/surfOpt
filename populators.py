import random as rd

# created a simple real-valued individual randomly in a specified rnge
def realInd(lls, uls):
  return [rd.uniform(lls[g], uls[g]) for g in range(len(lls))]