class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode: 
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    """
    dummy = ListNode(0, head)

    leftPtr = dummy 
    rightPtr = head

    while n > 0 and rightPtr:
        rightPtr = rightPtr.next
        n -= 1
    
    while rightPtr: 
        leftPtr = leftPtr.next
        rightPtr = rightPtr.next
    
    leftPtr.next = leftPtr.next.next

    return dummy.next 

# testNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
testNode = ListNode(1)
print("Result:", removeNthFromEnd(testNode, 1))