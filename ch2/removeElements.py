from linkedlist import SingleLinkedList,ListNode

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head==None:
        return None
    dummy=ListNode(0)
    dummy.next=head
    node=dummy
    while node.next:
        if node.next.data==val:
            node.next=node.next.next
        else:
            node=node.next
    return dummy.next

l=SingleLinkedList()
l.add_list_item(1)
print(removeElements(l.root,1))