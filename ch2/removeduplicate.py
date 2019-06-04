from linkedlist import SingleLinkedList

def removeduplicate(ll):
	dup_dict={}
	curr=ll.root
	prev=None
	while curr is not None:
		if curr.data not in dup_dict:
			dup_dict[curr.data]=True
		else:
			#do delete
			prev.next=curr.next
		prev=curr
		curr=curr.next

def remove(ll):
	#equals to two for loop
	curr=ll.root
	while curr is not None:
		runner=curr
		while runner.next is not None:
			if runner.next.data==curr.data:
				runner.next=runner.next.next
			else:
				runner=runner.next
		curr=curr.next

l=SingleLinkedList()
l.add_list_item(2)
l.add_list_item(3)
l.add_list_item(1)
l.add_list_item(3)
l.add_list_item(1)
l.add_list_item(1)
l.add_list_item(5)
l.printall()
