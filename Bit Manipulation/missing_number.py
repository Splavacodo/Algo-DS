class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing_num = len(nums)

        for i in range(len(nums)):
            missing_num ^= (i ^ nums[i])
        
        return missing_num 