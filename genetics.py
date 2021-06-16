import random as rd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# a DE/rand/1/exp GA
class diffEvolver:
    def __init__(self, ps, F, cp, nfe, rng = 123):
        self.ps = ps
        self.F = F
        self.cp = cp
        self.nfe = nfe
        self.rng = rng
        self.pop = []
        self.evals = []
    
    def setPopulator(self, populator):
        self.populator = populator
    
    def setReproduction(self, reproduction):
        self.reproduction = reproduction
    
    def setSurvival(self, survival):
        self.survival = survival
    
    def setDistance(self, distance):
        self.distance = distance
    
    def setSeed(self, rng):
        self.rng = rng
    
    def verbosity(self, ngen, nevals, population, evaluations):
        meanFit = sum(evaluations) / len(evaluations)
        print('GENERATION: ', str(ngen), ' / Fitness evaluations: ', nevals, '. Mean fitness is ', '{:.2f}'.format(meanFit), ", Showing top 10 individuals...", sep = '')
        top = (-np.array(evaluations)).argsort()
        for i in range(10):
            ind = ['{:.2f}'.format(d) for d in population[top[i]]]
            print("\t", "Fitness: ", '{:.2f}'.format(evaluations[top[i]]), " / Genotype: ", str(ind), sep = '')

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
        