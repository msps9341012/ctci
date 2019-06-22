from linkedlist import SingleLinkedList

def reverse(ll):
	previous=None
	node=ll.root.copy()
	while node:
		next=node.next
		node.next=previous
		previous=node
		if next:
			node=next.copy()
		else:
			break
	return previous





def palindrome(ll):
	r=reverse(ll)
	node=ll.root
	while r:
		print(r.data,node.data)
		if r.data!=node.data:
			return False
		else:
			r=r.next
			node=node.next
	return True

l=SingleLinkedList()
l.add_list_item('1')
l.add_list_item('1')
l.add_list_item('2')
l.add_list_item('1')

l.printall()

r=reverse(l)
tmp=""
node=r
while node is not None:
	tmp=tmp+str(node.data)+'->'
	node=node.next
print(tmp[:-2])



print(palindrome(l))


