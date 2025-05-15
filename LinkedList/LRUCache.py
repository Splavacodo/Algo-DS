class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}

        self.least_recent = Node(0, 0)
        self.most_recent = Node(0, 0)

        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent


    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
            self.insert(self.key_to_node[key])

            return self.key_to_node[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
        
        self.key_to_node[key] = Node(key, value)
        self.insert(self.key_to_node[key])

        if len(self.key_to_node) > self.capacity:
            lru = self.least_recent.next

            self.remove(lru)
            del self.key_to_node[lru.key]
        
    
    def remove(self, node):
        prev = node.prev
        next = node.next

        next.prev = prev
        prev.next = next


    def insert(self, node):
        prev = self.most_recent.prev
        next = self.most_recent

        node.prev = prev
        node.next = next

        prev.next = node
        next.prev = node