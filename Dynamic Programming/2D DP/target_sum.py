class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        match_cache = {}

        def dfs(i, curr_total):
            if i == len(nums):
                return 1 if curr_total == target else 0
            elif (i, curr_total) in match_cache:
                return match_cache[(i, curr_total)]
            
            match_cache[(i, curr_total)] = dfs(i + 1, curr_total + nums[i]) + dfs(i + 1, curr_total - nums[i])

            return match_cache[(i, curr_total)]

        return dfs(0, 0)
