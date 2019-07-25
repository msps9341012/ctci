def minProduct3(a,b):
    bigger = b if a < b else a #a < b ? b : a
    smaller = a if a < b else b #a < b ? a : b
    return minProduct3Helper(smaller, bigger)

def minProduct3Helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1
    halfProd = minProduct3Helper(s,bigger)
    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger
