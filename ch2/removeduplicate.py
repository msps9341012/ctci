from linkedlist import SingleLinkedList

'''
需要考慮[1,1,1]
或是[1,2,2,1]
要check 重連的那個是否也為重複
'''
def removeduplicate(ll):
	dup_dict={}
	curr=ll.root
	prev=None
	while curr is not None:
		if curr.data not in dup_dict:
			dup_dict[curr.data]=True
			prev=curr
		else:
			#do delete
			prev.next=curr.next
		curr=curr.next
def remove_duplicates(head):
  node = head
  if node:
    values = {node.data: True}
    while node.next:
      if node.next.data in values:
        node.next = node.next.next
      else:
        values[node.next.data] = True
        node = node.next
  return head



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
l.add_list_item(1)
l.add_list_item(1)

l.printall()
removeduplicate(l)
l.printall()
