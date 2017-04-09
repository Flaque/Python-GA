
letter_map = {
'a' : 0,
'b' : 1,
'c' : 2,
'd' : 3,
'e' : 4,
'f' : 5,
'g' : 6,
'h' : 7
}

class Graph:

    def __init__(self, path):

        # Read the graph
        self.array = []
        with open("graph.txt") as f:
            lines = f.readlines()

            for line in lines:
                self.array.append(line.split(" "))

    def costOf(self, gene):
        """ Computes the cost of a gene for the graph """

        cost = 0
        for i in range(0, len(gene)-1):
            first = letter_map[gene[i]]
            second = letter_map[gene[i+1]]
            cost += int(self.array[first][second])
        return cost
