def printbinary(num):
	if num>=1 or num<=0:
		return "Error"
	frac=0.5
	b=[]
	while num>0:
		if len(b)>32:
			return 'Insufficient precision'
		if num>=frac:
			b.append('1')
			num=num-frac
		else:
			b.append('0')
		frac=frac/2
	return '0.'+''.join(b)

print(printbinary(0.25))

