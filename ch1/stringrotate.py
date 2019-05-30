def isSubstring(s1, s2):
	for i in range(len(s1)):
		tmp=s1[i:]+s1[:i]
		if tmp==s2:
			return True
	return False


data = [
('waterbottle', 'erbottlewat', True),
('tabletop', 'toptable', True),
('tabletop', 'optalbet', False)
]

wrong=0
for i in data:
  if isSubstring(i[0],i[1])!=i[2]:
    wrong=wrong+1
print(wrong)