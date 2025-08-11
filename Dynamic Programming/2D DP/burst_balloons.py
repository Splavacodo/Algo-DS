class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        def dfs(left, right):
            if left > right:
                return 0
            elif dp[left - 1][right - 1] != 0:
                return dp[left - 1][right - 1]
            
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                dp[left - 1][right - 1] = max(dp[left - 1][right - 1], coins)
            
            return dp[left - 1][right - 1]
        
        return dfs(1, len(nums) - 2)
