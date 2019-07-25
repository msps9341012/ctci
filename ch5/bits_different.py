
def bits_different_1(a, b):
  different = a ^ b
  count = 0
  while different:
  	'''
  	n &-n returns the rightmost 1 bit in n.
  	傳回最右邊的後 再用xor把它消掉(因為一樣)
  	'''
    different ^= different & -different
    print(different)
    count += 1
  return count

bits_different_1(29,15)