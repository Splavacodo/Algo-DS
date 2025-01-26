class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(curr):
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        connected_count = 0

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                connected_count += 1
        
        return connected_count
