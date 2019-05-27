import sys

def palindrome_permutation(string):
	string=string.replace(' ','').lower()

	count_odd=0
	vol_dict={}
	for i in string:
		if i in vol_dict:
			vol_dict[i]=vol_dict[i]+1
		else:
			vol_dict[i]=1
		if vol_dict[i]%2==1:
			count_odd=count_odd+1
		else:
			count_odd=count_odd-1
	return count_odd<=1

print(palindrome_permutation(sys.argv[1]))


