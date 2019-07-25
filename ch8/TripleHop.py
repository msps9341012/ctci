def TripleHop(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return TripleHop(x - 1) + TripleHop(x - 2) + TripleHop(x - 3)

def TripleHop_dp(x):
	res=[0]*(x+1)
	if x==0:
		return 1
	res[0]=1
	res[1]=1
	res[2]=2
	for i in range(3,x+1):
		res[i]=res[i-1]+res[i-2]+res[i-3]
	return res[x]



