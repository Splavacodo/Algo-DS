class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        all_subsets = []
        curr_subset = []

        def find_subsets(idx):
            if idx == len(nums):
                all_subsets.append(curr_subset.copy())
                return 
            
            curr_subset.append(nums[idx])
            find_subsets(idx + 1)

            curr_subset.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            
            find_subsets(idx + 1)
        
        find_subsets(0)
        return all_subsets