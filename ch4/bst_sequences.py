
def bst_sequences(bst):
  return bst_sequences_partial([], [bst])
  
def bst_sequences_partial(partial, subtrees):
  if not len(subtrees):
    return [partial]
  sequences = []
  for index, subtree in enumerate(subtrees):
    next_partial = partial + [subtree.data]
    next_subtrees = subtrees[:index] + subtrees[index+1:]
    print(next_partial,next_subtrees)
    if subtree.left:
      next_subtrees.append(subtree.left)
    if subtree.right:
      next_subtrees.append(subtree.right)
    sequences += bst_sequences_partial(next_partial, next_subtrees)
  return sequences

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
  
x=Node(7,Node(4,Node(5)),Node(9))


print(bst_sequences(x))