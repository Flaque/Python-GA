from ga import GA
import random
from chromosome import Chromosome
from graph import Graph
import pmx
import cx
import numpy

class TravelingSalesman(GA):
    """ Abstract class, don't run directly """

    def __init__(self, params_path, graph_path, stopping_point):
        GA.__init__(self, params_path)
        self.chars = list('abcdefgh')[:self.params["NumGenes"]]
        self.graph = Graph(graph_path)
        self.stopping_point = stopping_point

    def init_pop(self):

        for i in range(self.params["NumChromesInit"]):

            # Create a new random gene
            chars = self.random_letters(self.params["NumGenes"], False)
            chrome = Chromosome(''.join(chars))
            chrome.cost = self.compute_cost(chrome)

            # And add to pop
            self.population.append(chrome)

    def compute_cost(self, chrome):
        return self.graph.costOf(str(chrome))

    def is_close_enough(self, chrome):
        if self.compute_cost(chrome) <= self.stopping_point:
            return True
        else:
            return False

    def mutate(self):

        howMany = int( len(self.population) * self.params["MutFact"])

        for chrome in random.sample(self.population, howMany):

            # Pick a random gene to mutate
            x = random.randint(0, self.params["NumGenes"] - 1)
            y = random.randint(0, self.params["NumGenes"] - 1)
            chrome.genes[x], chrome.genes[y] = chrome.genes[y], chrome.genes[x]
            chrome.cost = self.compute_cost(chrome)


class TravelingSalesman_PMX_TopDown(TravelingSalesman):

    def mate(self, pairs):
        self.population = pmx.mate(pairs)

    def pair(self):
        pop_clone = list(self.population) # Clone the list

        pop_clone = pop_clone[:self.params["NumChromes"]] # Only take the worthy

        # Shuffle the list up
        random.shuffle(pop_clone)

        # Split into two
        left, right = pop_clone[:len(pop_clone)/2], pop_clone[len(pop_clone)/2:]

        # Pair the right with the left
        return zip(left, right)

# ga = TravelingSalesman_PMX_TopDown('params.json', 'graph.txt', 3800)
# ga.init_pop()
# ga.sort()
#
# iterations, chrome = ga.evolve(True)
# print '\ntotal iterations:', iterations, 'chrome:', chrome


class TravelingSalesman_PMX_Tourn(TravelingSalesman):

    def mate(self, pairs):
        self.population = pmx.mate(pairs)

    def pair(self):
        # TODO
        pass

class TravelingSalesman_CX_TopDown(TravelingSalesman):

    def mate(self, pairs):
        self.population = cx.mate(pairs)
        pass

    def pair(self):
        pop_clone = list(self.population) # Clone the list

        pop_clone = pop_clone[:self.params["NumChromes"]] # Only take the worthy

        # Shuffle the list up
        random.shuffle(pop_clone)

        # Split into two
        left, right = pop_clone[:len(pop_clone)/2], pop_clone[len(pop_clone)/2:]

        # Pair the right with the left
        return zip(left, right)

ga = TravelingSalesman_CX_TopDown('params.json', 'graph.txt', 3800)
ga.init_pop()
ga.sort()

iterations, chrome = ga.evolve(True)
print '\ntotal iterations:', iterations, 'chrome:', chrome


class TravelingSalesman_CX_Tourn(TravelingSalesman):

    def mate(self, pairs):
        self.population = cx.mate(pairs)
        pass

    def pair(self):
        # TODO
        pass
