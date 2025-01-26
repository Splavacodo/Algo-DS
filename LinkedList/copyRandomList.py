class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # create a hashmap that maps each original node to a copy of the same node
        node_copies = {None: None}

        curr = head
        while curr:
            node_copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = node_copies[curr]
            copy.next = node_copies[curr.next]
            copy.random = node_copies[curr.random]
            curr = curr.next
        
        return node_copies[head]