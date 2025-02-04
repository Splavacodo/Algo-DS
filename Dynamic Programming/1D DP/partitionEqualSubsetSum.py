class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        dp = set([0])
        target = total / 2

        for num in nums:
            if num > target:
                return False
            
            nextDp = set()

            for subset_total in dp:
                if subset_total + num == target:
                    return True
                elif subset_total + num < target:
                    nextDp.add(subset_total + num)
                
                nextDp.add(subset_total)
            
            dp = nextDp
        
        return False