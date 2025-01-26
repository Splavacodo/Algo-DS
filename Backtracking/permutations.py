class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        def find_permutations(nums, idx):
            if idx == len(nums):
                permutations.append(nums.copy())
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                find_permutations(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
            
        find_permutations(nums, 0)
        return permutations