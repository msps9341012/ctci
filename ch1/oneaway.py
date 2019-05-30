import sys
def one_away(str1, str2):
  if len(str1)-len(str2)==1: #remove
    return check_i_r(str2,str1)
  elif len(str2)-len(str1)==1: #insert
    return check_i_r(str1,str2)
  elif len(str1)==len(str2): #replace
    return checkreplace(str1,str2)
  else:
    return False


def check_i_r(str1, str2):
    edited = False
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

  
def checkreplace(str1, str2):
  diff_count=0
  for i, j in zip(str1,str2):
    if i!=j:
      diff_count=diff_count+1
  return (diff_count<=1)


data = [
('pale', 'ple', True),
('pales', 'pale', True),
('pale', 'bale', True),
('paleabc', 'pleabc', True),
('pale', 'ble', False),
('a', 'b', True),
('', 'd', True),
('d', 'de', True),
('pale', 'pale', True),
('pale', 'ple', True),
('ple', 'pale', True),
('pale', 'bale', True),
('pale', 'bake', False),
('pale', 'pse', False),
('ples', 'pales', True),
('pale', 'pas', False),
('pas', 'pale', False),
('pale', 'pkle', True),
('pkle', 'pable', False),
('pal', 'palks', False),
('palks', 'pal', False)
]
wrong=0
for i in data:
  if one_away(i[0],i[1])!=i[2]:
    wrong=wrong+1
print(wrong)

