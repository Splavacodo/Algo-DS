class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return None
        
        return self.split_lists(lists, 0, len(lists) - 1)
    
    def split_lists(self, lists, left, right): 
        if left > right:
            return None
        elif left == right: 
            return lists[left]
        
        mid = left + (right - left) // 2

        left_half = self.split_lists(lists, left, mid)
        right_half = self.split_lists(lists, mid + 1, right)

        return self.merge(left_half, right_half)

    def merge(self, first_linked, second_linked):
        behind_head = ListNode(0)
        curr = behind_head

        while first_linked and second_linked:
            if first_linked.val <= second_linked.val:
                curr.next = first_linked
                first_linked = first_linked.next
            else:
                curr.next = second_linked
                second_linked = second_linked.next
            
            curr = curr.next
        
        if first_linked:
            curr.next = first_linked
        else:
            curr.next = second_linked
        
        return behind_head.next