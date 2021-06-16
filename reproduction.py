import random as rd

# In DE, all individuals in the population are parents. For each parent, 3 other
# individuals are selected and a new individual is obtained by mutating these
# 3 with m = i1 + F(i2, i3) where F is a scaling factor and the operations are
# carried out component (dimension) wise. The mutated individual m and the parent
# are used for a crossover in which the offspring accepts components of the parent
# unless a radomly generated float [0, 1] is lesser than the probability of
# crossover in which case the offspring accepts the component from the mutated
# individual in an initially randomly determined dimension of the offspring's solution
# vector; afterwards, contiguous dimensions are visited and assigned in the same
# manner in a circular way [3]. This code implements this procedure in a slightly
# more optimized way than described. 
def DERandOneExp(parent_indx, population, F, cprob, lls, uls):
  P = population.copy()
  dim = len(lls)

  parent = P.pop(parent_indx)
  offspring = parent.copy()
  donors = rd.sample(P, 3)
  n = rd.randint(0, dim - 1)
  j = 0
  while j < dim and rd.random() < cprob:
    offspring[n] = donors[0][n] + (F * (donors[1][n] - donors[2][n]))
    if offspring[n] < lls[n]:
      offspring[n] = lls[n]
    if offspring[n] > uls[n]:
      offspring[n] = uls[n]
    n = (n + 1) % dim
    j += 1
  return offspring
