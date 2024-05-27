class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode: 
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together 
    the nodes of the first two lists.

    Return the head of the merged linked list.
    """
    newNode = ListNode()
    currNode = newNode 

    while list1 and list2: 
        if list1.val < list2.val: 
            currNode = list1
            list1 = list1.next
        else: 
            currNode = list2
            list2 = list2.next
        
        currNode = currNode.next 
    # Need to check if either the list1 node or list2 node is null
    # Since the lists are sorted, one node can be added to the end
    # of the other
    if list1: 
        currNode.next = list1
    elif list2: 
        currNode.next = list2
    
    return newNode.next