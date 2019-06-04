# !/usr/bin/python
# coding:utf-8

from linkedlist import SingleLinkedList
def deletemiddlenode(node):
	if node is None or node.next is None:
		return False
	#直接蓋過去
	next=node.next
	node.data=next.data
	node.next=node.next.next 
	return True


l=SingleLinkedList()
l.add_list_item(1)
l.add_list_item(2)
l.add_list_item(3)
l.add_list_item(4)
l.add_list_item(5)
l.add_list_item(6)
l.add_list_item(7)

l.printall()
#print(returnkthtolast(l,4))
node=l.root.next.next.next
deletemiddlenode(node)
l.printall()
