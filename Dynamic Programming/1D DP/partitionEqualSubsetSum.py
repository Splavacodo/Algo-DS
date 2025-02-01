class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        dp = set([0])
        target = total / 2

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()

            for subset_total in dp:
                if subset_total + nums[i] == target:
                    return True
                
                nextDp.add(subset_total)
                nextDp.add(subset_total + nums[i])
            
            dp = nextDp
        
        return False