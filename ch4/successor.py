def successor(node):
  if not node:
    return None
  child = node.right
  if child:
    while child.left:
      child = child.left
  if child:
    return child
  x=node.parent
  while x!=None and x.left!=node:
    node=x
    x=x.parent #default為None 所以還是可以處理
  return x

class Node():
  def __init__(self, data, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.parent = None
    if self.left:  self.left.parent  = self
    if self.right: self.right.parent = self


x=Node(22, Node(11,Node(8),Node(12)), Node(33))
print(successor(x.right))

'''
  self.assertEqual(successor(Node(22, Node(11))), None)
  self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
  self.assertEqual(successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
  self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
  self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)
'''