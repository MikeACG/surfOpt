import random as rd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# implements a differential evolution GA
class diffEvolver:
    def __init__(self, ps, F, cp, nfe, rng = 123):
        self.ps = ps # population size
        self.F = F # scaling factor
        self.cp = cp # crossover probability
        self.nfe = nfe # number of function evaluations
        self.rng = rng # random seed for reproducibility
        self.pop = [] # keeps the population after evolution
        self.evals = [] # keeps the evaluations of the population after evolution
    
    # sets the function to initialize individuals
    def setPopulator(self, populator):
        self.populator = populator
    
    # sets the DE reproduction method
    def setReproduction(self, reproduction):
        self.reproduction = reproduction
    
    # sets the survival method after reproduction and before next iteration of evolution
    def setSurvival(self, survival):
        self.survival = survival
    
    # sets the distance fucntion for survival calculation
    def setDistance(self, distance):
        self.distance = distance
    
    # allows for changing the rng seed
    def setSeed(self, rng):
        self.rng = rng
    
    # prints progress of evolution process
    def verbosity(self, ngen, nevals, population, evaluations):
        meanFit = sum(evaluations) / len(evaluations)
        print('GENERATION: ', str(ngen), ' / Fitness evaluations: ', nevals, '. Mean fitness is ', '{:.2f}'.format(meanFit), ", Showing top 10 individuals...", sep = '')
        top = (-np.array(evaluations)).argsort()
        for i in range(10):
            ind = ['{:.2f}'.format(d) for d in population[top[i]]]
            print("\t", "Fitness: ", '{:.2f}'.format(evaluations[top[i]]), " / Genotype: ", str(ind), sep = '')

    # GA
    def evolve(self, surf):
        rd.seed(self.rng)
        pop = [self.populator(surf.dlims, surf.ulims) for i in range(self.ps)]
        nevals = 0
        gen = 1
        while nevals < self.nfe:
            evals = [surf.f(i) for i in pop]
            if nevals % (np.floor( (10 * self.nfe) / 100 )) == 0:
                self.verbosity(gen, nevals, pop, evals)
            new_pop = pop.copy()
            for i in range(self.ps):
                offspring = self.reproduction(i, pop, self.F, self.cp, surf.dlims, surf.ulims)
                replace = self.survival(offspring, surf.f(offspring), pop, evals, self.distance)
                if replace > -1:
                    new_pop[replace] = offspring
            pop = new_pop
            nevals += self.ps * 2
            gen += 1
        print("DONE, FINAL POPULATION:")
        self.verbosity(gen, nevals, pop, evals)
        self.pop = pop
        self.evals = evals
        