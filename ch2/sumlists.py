from linkedlist import SingleLinkedList,ListNode

def sumlists(node1,node2):
	carry=0
	result_head, result_node = None, None
	while node1 or node2 or carry:
		result=carry
		if node1:
			result=result+node1.data
			node1=node1.next
		if node2:
			result=result+node2.data
			node2=node2.next
		if result_node:
			result_node.next = ListNode(result % 10)
			result_node = result_node.next
		else:
			result_node = ListNode(result % 10)
			result_head = result_node
		carry = result//10

	return result_head



l1=SingleLinkedList()
l1.add_list_item(2)
l1.add_list_item(3)
l1.printall()
l2=SingleLinkedList()
l2.add_list_item(1)
l2.add_list_item(8)
l2.add_list_item(6)
l2.printall()
r=sumlists(l1.root,l2.root)
tmp=""
while r is not None:
	tmp=tmp+str(r.data)+'->'
	r=r.next
print(tmp[:-2])
