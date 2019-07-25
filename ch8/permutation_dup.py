def permuteUnique(self,list1):
    if len(list1)<2:
        return [list1]
    res=[list1[:2],list1[:2][::-1]]
    if res[0]==res[1] and len(list1)==2:
        res.pop()
        return res
    for i in range(2,len(list1)):
        res=self.gen_per(res,[list1[i]])
    return res

def gen_per(self,res,add_s):
    tmp=[]
    for string in res:
        for i in range(len(string)+1):
            if string[:i]+add_s+string[i:] not in tmp:
                tmp.append(string[:i]+add_s+string[i:])
    return tmp


def permute(nums):
    return partial_permutations([], sorted(nums))

def partial_permutations(partial, letters_left):
    if len(letters_left) == 0:
        return [partial]
    permutations = []
    previous=None
    for i, letter in enumerate(letters_left):
    	if letter==previous:
    		continue
        next_letters_left = letters_left[:i] + letters_left[(i+1):]
        permutations += partial_permutations(partial + [letter], next_letters_left)
    	previous=letter
    return permutations

print(permute([2,2,1]))