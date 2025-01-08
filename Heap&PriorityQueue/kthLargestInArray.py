from random import choice

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(some_nums, k):
            pivot = choice(some_nums)

            smaller_nums = []
            bigger_nums = []
            same_nums = []

            for num in some_nums:
                if num < pivot:
                    smaller_nums.append(num)
                elif num > pivot:
                    bigger_nums.append(num)
                else:
                    same_nums.append(num)

            smol_len = len(smaller_nums)

            if smol_len <= k < len(same_nums) + smol_len:
                return pivot
            elif smol_len + 1 > k:
                return quick_select(smaller_nums, k)
            else:
                return quick_select(bigger_nums, k - (smol_len + len(same_nums)))
        
        return quick_select(nums, k)