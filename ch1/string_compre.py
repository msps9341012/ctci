import sys

def compre(string):
	count=1
	string=string+' '
	final_string=""
	for i in range(len(string)-1):
		if string[i]==string[i+1]:
			count=count+1
		else:
			final_string=final_string+string[i]+str(count)
			count=1
	if len(final_string)<len(string):
		return final_string
	else:
		return string[:-1]

print(compre(sys.argv[1]))
