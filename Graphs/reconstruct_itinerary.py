from collections import deque

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = {src : deque() for src, _ in tickets}
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)
        
        itinerary = deque()

        def dfs(curr):
            if curr in adj:
                while adj[curr]:
                    dst = adj[curr].popleft()
                    dfs(dst)
                
            itinerary.appendleft(curr)

        dfs("JFK")

        return list(itinerary)