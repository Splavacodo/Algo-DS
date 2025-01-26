class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]
        
        return max(dp)