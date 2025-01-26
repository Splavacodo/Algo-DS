from collections import defaultdict, deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
def cloneGraph(node: Node) -> Node:
    if not node:
        return None
    
    # For bfs to create a queue and a set of visited nodes
    queue = deque([node])
    visited = set()

    # Also need a copy of the entire graph
    clones = defaultdict(Node)

    while queue: 
        currNode = queue.popleft()

        if currNode not in visited: 
            # Copy the val of the node
            clones[currNode].val = currNode.val

            # Then copy its neighbors
            for neighbor in currNode.neighbors: 
                clones[neighbor].val = neighbor.val
                clones[currNode].neighbors.append(clones[neighbor])
        
            queue.extend(currNode.neighbors)
            visited.add(currNode)
    
    return clones[node]