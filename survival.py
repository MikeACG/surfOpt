# In regular DE, the offspring only makes it to the next generation if it has
# higher fitness than its parent; however, a variant of DE is used (crowding DE).
# In this variant, the nearest neighbor to the offspring is found, 
# then the offspring replaces that neighbor in the population if its fitness is at least as good.
# This is done for every offspring right before advancing to the next generation.
# The distance is computed in genotype space.

def DEcrowd(offspring, offspring_eval, population, population_evals, df):
    distances = [df(offspring, i) for i in population]
    nn = distances.index(min(distances))
    replace = nn if offspring_eval >= population_evals[nn] else -1
    return replace