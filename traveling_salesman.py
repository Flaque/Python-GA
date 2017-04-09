from ga import GA
import random
from chromosome import Chromosome
from graph import Graph

class TravelingSalesman(GA):
    """ Abstract class, don't run directly """

    def __init__(self, params_path, graph_path, stopping_point):
        GA.__init__(self, params_path)
        self.graph = Graph(graph_path)
        self.stopping_point = stopping_point

    def compute_cost(self, chrome):
        return self.graph.costOf(str(chrome))

    def is_close_enough(self, chrome):
        if self.compute_cost(chrome) <= self.stopping_point:
            return True
        else:
            return False
