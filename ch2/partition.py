from linkedlist import SingleLinkedList

def partition(node,value):
	small_head=small_tail=None
	big_head=big_tail=None

	while node:
		if node.data<value:
			if small_head:
				small_tail.next=node
				small_tail=node
			else:
				small_head=node
				small_tail=node
		else:
			if big_head:
				big_tail.next=node
				big_tail=node
			else:
				big_head=node
				big_tail=node
		node=node.next
	small_tail.next=big_head
	print(big_tail.next.data)
	return small_head

def partition_2(node,value):
	head=node
	tail=node
	while node:
		next=node.next
		if node.data<value:
			node.next=head
			head=node
		else:
			tail.next=node
			tail=node
		node=next
	tail.next=None
	return head

l=SingleLinkedList()
l.add_list_item(3)
l.add_list_item(5)
l.add_list_item(8)
l.add_list_item(5)
l.add_list_item(10)
l.add_list_item(2)
l.add_list_item(1)

l.printall()

x=partition_2(l.root,5)

tmp=""
while x is not None:
	tmp=tmp+str(x.data)+'->'
	x=x.next
print(tmp[:-2])
