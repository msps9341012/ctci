import sys

def checkunique(string):
	count_dict={}
	for i in string:
		if i in count_dict:
			return False
		count_dict[i]=1
	return True

if __name__ == "__main__":
  print(checkunique(sys.argv[-1]))

