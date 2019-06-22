class Node():
	def __init__(self, left=None, right=None):
		self.left, self.right = left, right


def getheight(root):
	if root==None:
		return (True, 0)
	left_balanced,l=getheight(root.left)
	if not left_balanced:
		return(False, None)
	right_balanced,r=getheight(root.right)
	if (not right_balanced) or (abs(l - r) > 1):
		return(False, None)
	depth=max(l,r)+1
	return (True, depth)



print(getheight(Node(Node(),Node(Node(Node())))))
