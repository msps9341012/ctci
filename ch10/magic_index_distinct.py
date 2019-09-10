def magic_index_distinct(array):
  if len(array) == 0 or array[0] > 0 or array[-1] < len(array) - 1:
    return None
  return magic_index_distinct_bounds(array, 0, len(array))

def magic_index(array,lower,upper):
	if upper<lower:
		return -1
	middle = (lower + upper)//2
	if array[middle] == middle:
		return middle
	search_left=min(middle-1,array[middle])
	left=magic_index(array,lower,search_left)
	if left>=0:
		return left
	search_right=max(middle+1,array[middle])
	right=magic_index(array,search_right,upper)
	return right

print(magic_index([-10,-5,6,6,6,6,6,7,9,12,13],0,9))