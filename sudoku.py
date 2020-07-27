graph = []
domains = dict()
vars = []
assigned = dict()

def initVars():
    for i in range(9):
        for j in range(9):
            vars.append((i,j))
            domains[(i,j)] = {1,2,3,4,5,6,7,8,9}

def initGraph():
    for index1 in vars:
        for index2 in vars:
            if (index1 != index2 and (index1[0] == index2[0] or index1[1] == index2[1] or 
                (((index1[0] // 3) == (index2[0] // 3)) and ((index1[1] // 3) == index2[1] // 3)))):
                graph.append([index1, index2])

def arcConsistencyCSP():
    """
    Implement AC3 here
    """
    "*** YOUR CODE HERE ***"
    def revise(newDomain, var1, var2):
        d = newDomain.copy()
        revised = False
        newSet = set()
        # newSet2 = set()
        for val in d[var1]:
            satisfy = False
            for val2 in d[var2]:
                if val != val2:
                    satisfy = True
            if not satisfy:
                revised = True
            else:
                newSet.add(val)
        # for val in d[var2]:
        #     satisfy = False
        #     for val2 in d[var1]:
        #         if val != val2:
        #             satisfy = True
        #     if not satisfy:
        #         revised = True
        #     else:
        #         newSet2.add(val)
        d[var1] = newSet
        # d[var2] = newSet2
        return (revised, d)
    queue = graph.copy()
    newDomains = domains.copy()
    while len(queue) != 0:
        arc = queue.pop(0)
        r, newDomains = revise(newDomains, arc[0], arc[1])
        if r:
            if len(domains[arc[0]]) == 0:
                return dict()
            for a in graph:
                if (a[0] == arc[0] and a[1] != arc[1]) or (a[1] == arc[0] and a[0] != arc[1]):
                    if(queue.count(a) == 0):
                        queue.append(a)

    return newDomains

def backtrackingsearch():
    return backtrack(assigned)

def backtrack(assignment):
    def selectunassignedvariable():
        for i in range(9):
            for j in range(9):
                if (i,j) not in assigned:
                    return (i,j)

    global domains

    if len(assignment) == 81:
        return assignment
    var = selectunassignedvariable()
    oldDomain = domains.copy()
    for value in domains[var]:
        assignment[var] = value
        domains[var] = {value}
        domains = arcConsistencyCSP()
        if domains:
            result = backtrack(assignment)
            if result:
                return result
        domains = oldDomain.copy()
        del assignment[var]
    return dict()

def solveSudoku(sudokuBoard):

    initVars()
    initGraph()
    
    global domains

    for i in range(9):
        for j in range(9):
            if sudokuBoard[i][j] != 0:
                domains[(i, j)] = {sudokuBoard[i][j]}
                assigned[(i, j)] = sudokuBoard[i][j]
    
    domains = arcConsistencyCSP()
    
    result = backtrackingsearch()

    for key in result:
        sudokuBoard[key[0]][key[1]] = result[key]

    for row in sudokuBoard:
        print(row)
    return result
