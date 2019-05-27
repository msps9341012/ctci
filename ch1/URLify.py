import sys

def urlify(string, length):
	out=""
	for i in range(int(length)):
		if string[i]!=" ":
			out=out+string[i]
		else:
			out=out+"%20"
	return(out)

print(urlify(sys.argv[1],sys.argv[2]))


