from collections import defaultdict

from common import InputForDay

indata = InputForDay(3).get()

# The dict will save us from worrying about expensive array expansion.
panel = defaultdict(lambda: defaultdict(int))
intersections = []

wire1, wire2 = indata[0], indata[1]
dirmap = { "U": ( 0 , 1),
           "D": ( 0 ,-1),
           "L": (-1 , 0),
           "R": ( 1 , 0) }

# Mark the first wire on the panel.
ptrx, ptry = 0, 0
for i in wire1:
    d, val = i[0], int(i[1:])
    for j in range(val):
        direction = dirmap[d]
        ptrx += direction[0]
        ptry += direction[1]
        panel[ptrx][ptry] = 1

# Find the intersections by tracing the second wire's path
ptrx, ptry = 0, 0
for i in wire2:
    d, val = i[0], int(i[1:])
    for j in range(val):
        direction = dirmap[d]
        ptrx += direction[0]
        ptry += direction[1]
        if (1 == panel[ptrx][ptry]):
            intersections += [(ptrx, ptry)]

closestIntersection = min(map(lambda x: abs(x[0]) + abs(x[1]), intersections))
print("Part 1: {}".format(closestIntersection))

# Part 2
def countSteps(pos):
    # XD
    class BreakNested(Exception): pass
    # Count steps for the first wire
    nsteps = 0

    ptrx, ptry = 0, 0
    try:
        for i in wire1:
            d, val = i[0], int(i[1:])
            for j in range(val):
                direction = dirmap[d]
                ptrx += direction[0]
                ptry += direction[1]
                nsteps += 1
                if pos == (ptrx, ptry):
                    raise BreakNested

    except BreakNested: pass

    # Count steps for the second wire
    ptrx, ptry = 0, 0
    try:
        for i in wire2:
            d, val = i[0], int(i[1:])
            for j in range(val):
                direction = dirmap[d]
                ptrx += direction[0]
                ptry += direction[1]
                nsteps += 1
                if pos == (ptrx, ptry):
                    raise BreakNested

    except BreakNested: pass

    return nsteps


print("Part 2: {}".format(min(map(countSteps, intersections))))
