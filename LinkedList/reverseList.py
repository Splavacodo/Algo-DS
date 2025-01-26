class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList(head: ListNode) -> ListNode:
    if not head: 
        return None

    currNode = head
    valStack = []

    while currNode: 
        valStack.append(currNode.val)
        currNode = currNode.next
    
    newHead = ListNode()
    tempNode = newHead 

    while valStack: 
        tempNode.val = valStack.pop()
        if len(valStack) != 0: 
            tempNode.next = ListNode()
            tempNode = tempNode.next
    
    return newHead 

testHead = ListNode()
startNode = testHead

for count in range(2): 
    startNode.val = count
    startNode.next = ListNode()
    startNode = startNode.next 

reverseList(testHead)