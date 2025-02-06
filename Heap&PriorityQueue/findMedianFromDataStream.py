import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if (len(self.small) - len(self.large)) > 1:
            num_to_move = -heapq.heappop(self.small)
            heapq.heappush(self.large, num_to_move)
        
        if (len(self.large) - len(self.small)) > 1:
            num_to_move = -heapq.heappop(self.large)
            heapq.heappush(self.small, num_to_move)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            first_mid = -self.small[0]
            second_mid = self.large[0]
            
            return (first_mid + second_mid) / 2
