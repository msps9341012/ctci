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
l.add_list_item('a')
l.add_list_item('b')
l.add_list_item('c')
l.add_list_item('c')
l.add_list_item('c')
l.add_list_item('a')
l.printall()

r=reverse(l)
tmp=""
node=r
while node is not None:
	tmp=tmp+str(r.data)+'->'
	node=node.next
print(tmp[:-2])
l.printall()



print(palindrome(l))


