def DEcrowd(offspring, offspring_eval, population, population_evals, df):
  distances = [df(offspring, i) for i in population]
  nn = distances.index(min(distances))
  replace = nn if offspring_eval >= population_evals[nn] else -1
  return replace