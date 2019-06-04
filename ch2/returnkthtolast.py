from linkedlist import SingleLinkedList

def returnkthtolast(ll,k):
	runner=ll.root
	curr=ll.root
	for i in range(k):
		if runner is None:
			return None
		runner=runner.next
	while runner:
		runner=runner.next
		curr=curr.next
	return curr.data

def returnkthtolast_recursive(node,k):
	if node is None:
		return 0
	index=returnkthtolast_recursive(node.next,k)+1
	if index==k:
		print(node.data)
	return index
l=SingleLinkedList()
l.add_list_item(2)
l.add_list_item(3)
l.add_list_item(1)
l.add_list_item(3)
l.add_list_item(1)
l.add_list_item(1)
l.add_list_item(5)

l.printall()
#print(returnkthtolast(l,4))
returnkthtolast_recursive(l.root,4)

