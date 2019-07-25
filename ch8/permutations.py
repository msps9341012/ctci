def permutations(list1):
	res=[list1[:2],list1[:2][::-1]]
	print(res)
	for i in range(2,len(list1)):
		res=gen_per(res,[list1[i]])
	return res

def gen_per(res,add_s):
	tmp=[]
	for string in res:
		for i in range(len(string)+1):
			tmp.append(string[:i]+add_s+string[i:])
	res=tmp
	return res

def permute(nums):
    return partial_permutations([], nums)

def partial_permutations(partial, letters_left):
    if len(letters_left) == 0:
        return [partial]
    permutations = []
    for i, letter in enumerate(letters_left):
        next_letters_left = letters_left[:i] + letters_left[(i+1):]
        permutations += partial_permutations(partial + [letter], next_letters_left)
    return permutations

def permute2(nums):
    res = []
    dfs(sorted(nums), [], res)
    return res
    
def dfs(nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    previous=None
    for i in xrange(len(nums)):
    	if previous==nums[i]:
    		continue
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res) 
        previous=nums[i]

print(permute2([1,1]))