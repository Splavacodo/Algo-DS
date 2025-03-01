import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        heapq.heapify(nums)

        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]