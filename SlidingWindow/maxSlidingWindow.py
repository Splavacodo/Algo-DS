from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_in_windows = []
        queue = deque()

        left = 0
        for right in range(len(nums)):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            
            queue.append(right)

            if left > queue[0]:
                queue.popleft()
            
            if right + 1 >= k:
                max_in_windows.append(nums[queue[0]])
                left += 1
            
        return max_in_windows