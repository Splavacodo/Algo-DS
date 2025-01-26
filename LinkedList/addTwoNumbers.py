class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Original approach I tried which successfully solves the problem but is defintely not the most efficient.
        """
        l1_node_indexes = {}
        l2_node_indexes = {}

        i = 0
        curr = l1
        while curr:
            l1_node_indexes[curr] = i
            curr = curr.next
            i += 1
        
        i = 0
        curr = l2
        while curr:
            l2_node_indexes[curr] = i
            curr = curr.next
            i += 1
        
        sum = 0
        for node, idx in l1_node_indexes.items():
            sum += node.val * 10**idx
        
        for node, idx in l2_node_indexes.items():
            sum += node.val * 10**idx

        sum_head = ListNode()
        curr = sum_head
        for _ in range(len(str(sum))):
            curr.val = sum % 10
            if sum // 10 != 0:
                curr.next = ListNode()
                curr = curr.next
            sum = sum // 10
        
        return sum_head