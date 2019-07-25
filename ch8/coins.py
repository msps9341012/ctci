def makechange(n,coin_list,index):
	if index>=len(coin_list)-1:
		return 1
	amount=coin_list[index]
	ways=0
	i=0
	while i*amount<=n:
		ways=ways+makechange(n-i*amount,coin_list,index+1)
		i=i+1
	return ways

def coins(n):
	print(makechange(n,[5,2,1],0))
