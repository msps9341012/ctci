class ListNode():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next

class TreeNode():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.depth = None

node_h = TreeNode('H')
node_g = TreeNode('G')
node_f = TreeNode('F')
node_e = TreeNode('E', node_g)
node_d = TreeNode('D', node_h)
node_c = TreeNode('C', None, node_f)
node_b = TreeNode('B', node_d, node_e)
node_a = TreeNode('A', node_b, node_c)


def list_of_depths(binary_tree):
	if not binary_tree:
		return []
	lists = []
	queue = []
	current_depth = -1
	current_tail = None
	node = binary_tree
	node.depth = 0
	while node:
		if node.depth == current_depth:
			current_tail.next = ListNode(node.data)
			current_tail = current_tail.next
		else:
			current_depth = node.depth
			current_tail = ListNode(node.data)
			lists.append(current_tail)
		for child in [node.left, node.right]:
			if child:
				child.depth = node.depth + 1
				queue.append(child)
		if len(queue)==0:
			break
		node = queue.pop(0)
	return lists


x=list_of_depths(node_a)
print(x[1].next.data)
