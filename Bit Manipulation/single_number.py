class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_num = 0

        for num in nums:
            single_num = num ^ single_num
        
        return single_num