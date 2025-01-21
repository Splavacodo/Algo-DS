from collections import defaultdict, deque

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) > n:
            return False
        
        adj = [[] for _ in range(len(edges))]

        for first_node, second_node in edges:
            adj[first_node].append(second_node)
            adj[second_node].append(first_node)
        
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)

            for neighbor in adj[curr]:
                if neighbor == prev:
                    continue
                elif not dfs(neighbor, curr):
                    return False
        
            return True
        
        return dfs(0, -1) and len(visited) == n