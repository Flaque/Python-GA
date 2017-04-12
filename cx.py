from random import randint

def _subsection(item):
    L = list(range(0, len(item)-1))
    left = randint(0, len(L) - 1)
    right = randint(left + 1, len(L))
    return left, right

def _get_replaced_item(left, right, child, gene, relation_map):

    # Hit a base case
    if gene not in relation_map:
        return gene

    mapped = relation_map[gene]
    if mapped not in child[left:right]:
        return mapped
    else:
        return _get_replaced_item(left, right, child, mapped, relation_map)

def _map(left, right, mother, father):
    return dict(zip(father[left:right], mother[left:right]))

def _getIndex(item, child, left, right):

    # Search left
    for i in range(0, left):
        if child[i] == item:
            return i

    # Search right
    for i in range(right, len(child)):
        if child[i] == item:
            return i


def _swap_leftover_genes(left, right, mothers_child, fathers_child):
    father_map = _map(left, right, mothers_child, fathers_child)

    # Swap left versions
    for i in range(0, left):
        gene = fathers_child[i]
        mother_gene = _get_replaced_item(left, right, fathers_child, gene, father_map)

        fathers_child[i] = mother_gene
        m_index = _getIndex(mother_gene, mothers_child, left, right)
        mothers_child[m_index] = gene

    for i in range(right, len(fathers_child)):
        gene = fathers_child[i]
        mother_gene = _get_replaced_item(left, right, fathers_child, gene, father_map)

        fathers_child[i] = mother_gene
        m_index = _getIndex(mother_gene, mothers_child, left, right)
        mothers_child[m_index] = gene

    return fathers_child, mothers_child


def _mate_one(pair):
    mother, father = pair
    left, right = _subsection(mother)
   

    # Create copies (children) so we don't effect the original
    mothers_child = list(mother)
    fathers_child = list(father)
    index1 = random.randint(1, len(mothers_child)- 2)
    index2 = random.randint(1, len(fathers_child)- 2)

    if index1 > index2: index1, index2 = index2, index1 #swap indices

    #take the gene sequence from one point and connect it to the indices at
    #the other
    mothers_child = father[:index1] + mother[index1:index2] + father[index2:]
    fathers_child2 = mother[:index1] + father[index1:index2] + mother[index2:]

    return fathers_child, mothers_child

def mate(pairs):
    people = []
    for mother, father in pairs:
        child1, child2 = _mate_one(pair)
        people += [mother, father, child1, child2]
    return people
