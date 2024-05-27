class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None: 
    """
    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    """
    # Potential approach...
    # Check if there's only one node in the list, if there is return the head
    if not head.next: 
        return head 

    # Find out how many nodes are in the linked list first 
    currNode = head
    numNodes = 0 
    while currNode: 
        numNodes += 1
        currNode = currNode.next 
    
    # Next, add the second half of the list to a stack 
    currNum = 1
    secondHalf = numNodes//2 
    currNode = head
    secondHalfNodes = []
    while currNode: 
        if currNum > secondHalf: 
            secondHalfNodes.append(currNode)

        currNum += 1
        currNode = currNode.next 
    
    # Assuming the node index starts at 0, each even indexed node will have their next node replaced
    # by the node that's on the top of the stack
    currIndex = 0 
    currNode = head 
    while currNode: 
        if currIndex == numNodes - 1: 
            currNode.next = None 
        elif currIndex%2 == 0 and secondHalfNodes: 
            oldNode = currNode.next 
            currNode.next = secondHalfNodes.pop()
            currNode = currNode.next
            currNode.next = oldNode 
        else: 
            currNode = currNode.next 
        
        currIndex += 1