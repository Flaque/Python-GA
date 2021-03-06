import parameters
from chromosome import Chromosome
import numpy
import random
from string import lowercase

class GA:

    def __init__(self, param_path):
        self.params = parameters.read(param_path)
        self.chars = list(lowercase) # Should be overwritten by subclass
        self.population = []

    def random_letters(self, amount, replace=True):
        return numpy.random.choice(self.chars, amount, replace=replace)

    def sort(self):
        self.population = sorted(self.population, key=lambda x: x.cost)

    def init_pop(self):

        for i in range(self.params["NumChromesInit"]):

            # Create a new random gene
            chars = self.random_letters(self.params["NumGenes"])
            chrome = Chromosome(''.join(chars))
            chrome.cost = self.compute_cost(chrome)

            # And add to pop
            self.population.append(chrome)

    def mutate(self):

        howMany = int( len(self.population) * self.params["MutFact"])

        for chrome in random.sample(self.population, howMany):

            # Pick a random gene to mutate
            i = random.randint(0, self.params["NumGenes"] - 1)
            chrome.genes[i] = self.random_letters(1)[0]
            chrome.cost = self.compute_cost(chrome)

    def compute_cost_for_all(self):
        for chrome in self.population:
            chrome.cost = self.compute_cost(chrome)

    def evolve(self, andPrint=False):

        iterations = 0
        while iterations < self.params["NumIterations"]:
            pairs = self.pair()
            self.mate(pairs)
            self.mutate()
            self.compute_cost_for_all()
            self.sort()

            if andPrint:
                print ' '
                print 'i', iterations, 'best', self.population[0]
                print 'cost', self.population[0].cost
                print 'pop', self.population
                print '----'

            if self.is_close_enough(self.population[0]):
                break

            iterations += 1

        return iterations, self.population[0]


    def mate(self, pairs):
        """ Should be overwritten """
        return []

    def pair(self):
        """ Should be overwritten """
        return []

    def is_close_enough(self, chrome):
        """ Should be overwritten by subclass """

        return True

    def compute_cost(self, chrome):
        """ Should be overwritten by subclass, computes the cost of a single chromosome """
        return 1
