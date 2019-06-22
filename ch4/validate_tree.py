class Node():
	def __init__(self, data, left=None, right=None):
		self.data, self.left, self.right = data, left, right

 tree1 = Node(5,Node(3,Node(1),Node(4)),Node(7,Node(6),Node(8,None,Node(9))))


 def checkbst(root):
 	if root==None:
 		return None
 	if root.left:
 		l=root.left.data
 	if root.right:
 		r=root.right.data
 	if 	
 	if root.left.data<root.data and root.data<root.right.data
 		return 1
 	root.left

