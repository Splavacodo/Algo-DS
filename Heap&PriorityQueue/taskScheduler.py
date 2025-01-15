from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = Counter(tasks)
        count_heap = [-count for count in task_counts.values()]
        heapq.heapify(count_heap)

        queue = deque()
        time = 0

        while count_heap or queue:
            time += 1

            if count_heap:
                new_count = heapq.heappop(count_heap) + 1

                if new_count != 0:
                    queue.append([new_count, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(count_heap, queue.popleft()[0])
        
        return time