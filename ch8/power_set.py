def power_set(set0):
	res=[]
	for i in set0:
		tmp=[]
		for j in res:
			tmp.append(j+[i])
		res=res+tmp
		res.append([i])
	return res

print(power_set({'a', 'b', 'c', 'd'}))


def getSubsets2(aset):
    allSubsets = []
    max = 1 << len(aset)
    for k in range(max):
        subset = convertIntToSet(k, aset)
        allSubsets.append(subset)
    return allSubsets

def convertIntToSet(x, aset):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1 and aset[index] not in subset:
            subset.append(aset[index])
        index += 1
        k >>= 1
    return subset

print(getSubsets2([1,2,3]))
