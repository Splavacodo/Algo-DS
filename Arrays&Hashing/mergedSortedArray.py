class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n - 1
        merged_idx = m + n - 1

        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[merged_idx] = nums1[left]
                left -= 1
            else:
                nums1[merged_idx] = nums2[right]
                right -= 1
            
            merged_idx -= 1
        