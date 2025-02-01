class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_min, curr_max = 1, 1
        res = max(nums)

        for num in nums:
            temp = curr_max
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(num * temp, num * curr_min, num)

            res = max(res, curr_max)
        
        return res