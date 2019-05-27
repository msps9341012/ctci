import sys

def checkunique(string):
	count_dict={}
	for i in string:
		if i in count_dict:
			return False #return 可以break for loop
		count_dict[i]=1
	return True


print(checkunique(sys.argv[-1]))

