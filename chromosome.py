
class Chromosome:

    def __init__(self, string):
        self.genes = list(string)
        self.cost = None

    def __repr__(self):
        """ Lets us print out a chromosome """
        return str(''.join(self.genes) + " " + str(self.cost))

    def __str__(self):
        """ Lets us do str(chrome) """
        return ''.join(self.genes)

    def __len__(self):
        return len(self.genes)

    def __eq__(self, other):
        """ Overrides default equality so we can do chrome1 == chrome2 """
        if not other:
            return False
        for index, gene in enumerate(other.genes):
            if gene != self.genes[index]:
                return False
        return True

    def __ne__(self, other):
        """ Overrides != so we can do chrome1 != chrome2 """
        return not self.__eq__(other)
