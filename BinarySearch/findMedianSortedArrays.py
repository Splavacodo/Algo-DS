class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m  

        while left <= right:
            partition_x = (left + right) // 2
            partition_y = (m + n + 1) // 2 - partition_x

            max_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            max_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]

            min_x = float('inf') if partition_x == m else nums1[partition_x]
            min_y = float('inf') if partition_y == n else nums2[partition_y]

            if max_x <= min_y and max_y <= min_x:
                if (m + n) % 2 == 0:
                    return (max(max_x, max_y) + min(min_x, min_y)) /2
                else:
                    return max(max_x, max_y)
            elif max_x > min_y:
                right = partition_x - 1
            else:
                left = partition_x + 1