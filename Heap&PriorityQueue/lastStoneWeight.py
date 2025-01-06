import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while stones:
            if len(stones) == 1:
                return stones[0] * -1
            
            first_weight = -1 * heapq.heappop(stones)
            second_weight = -1 * heapq.heappop(stones)

            if first_weight == second_weight:
                continue
            else:
                heapq.heappush(stones, -1*(first_weight - second_weight))
        
        return 0