from traveling_salesman import *


def test(genetic):

    # Test PMX + Tournamet
    ga = genetic('params.json', 'graph.txt', 3800)
    ga.init_pop()
    ga.sort()

    iterations, chrome = ga.evolve()
    print 'total iterations:', iterations, 'chrome:', chrome, 'cost:', chrome.cost


print "Testing PMX with Tournament"
test(TravelingSalesman_PMX_Tourn)
print '\n'

print "Testing PMX with Top Down"
test(TravelingSalesman_PMX_TopDown)
print '\n'

print "Testing Cycle CX with Tournament"
test(TravelingSalesman_CX_Tourn)
print '\n'

print "Testing Cycle CX with TopDown"
test(TravelingSalesman_CX_TopDown)
print '\n'
