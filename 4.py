from collections import defaultdict

# from common import InputForDay

# This time input was given right away, in the task description
# indata = InputForDay(4).get()
left  = 136818
right = 685979

# Convert a number to a list of digits.
digits = lambda n: [int(x) for x in str(n)]

def hasTwoAdjacent(n: list):
    for i, k in enumerate(n[1:]):
        if n[i] == k:
            return True
    return False

def neverDecreases(n: list):
    for i, k in enumerate(n[1:]):
        if n[i] > k:
            return False
    return True

ans = map(digits, range(left, 1 + right))
ans = filter(hasTwoAdjacent, ans)
ans = filter(neverDecreases, ans)
ans = list(ans)
print("Part 1: {}".format(len(ans)))

# Part 2

def hasExactlyTwoAdjacent(n: list):
    # Store adjacent digits and see if any of the digits repeat exactly two
    # times.
    d = defaultdict(int)
    for i in n:
        d[i] += 1
    return 2 in d.values()

print("Part 2: {}".format(len(list(filter(hasExactlyTwoAdjacent, ans)))))
