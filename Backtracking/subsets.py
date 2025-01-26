class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        cur_subset = []
        def create_subset(idx):
            if idx >= len(nums):
                res.append(cur_subset.copy())
                return 

            cur_subset.append(nums[idx])
            create_subset(idx + 1)

            cur_subset.pop()
            create_subset(idx + 1)
        
        create_subset(0)
        return res