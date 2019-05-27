import sys

def checkpermutation(string1, string2):
	if len(string1)==len(string2):
		vol={}
		for i in string1:
			if i in vol:
				vol[i]=vol[i]+1
			else:
				vol[i]=1
		for i in string2:
			if i not in vol:
				return False
			vol[i]=vol[i]-1
			if vol[i]==0:
				del vol[i]
		return len(vol)==0
	else:
		return False


print(checkpermutation(sys.argv[1],sys.argv[2]))

