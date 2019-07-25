def TripleHop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return TripleHop(x - 1) + TripleHop(x - 2) + TripleHop(x - 3)