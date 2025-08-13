import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        heap = []
        query_to_interval = {}
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(heap, (right - left + 1, right))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            query_to_interval[query] = heap[0][0] if heap else -1
        
        return [query_to_interval[query] for query in queries]
