class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            
            curr = curr.next
        
        prev = None
        curr = head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head.next = self.reverseKGroup(curr, k)
        return prev