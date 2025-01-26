def twoSum(nums: list[int], target: int) -> list[int]: 
    """
    Given an array of integers nums and an integer target, return indices of the two numbers 
    such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the 
    same element twice.

    You can return the answer in any order.

    Different Approaches: 
    Hashmap - 
    Go through every num in the nums list and check for the difference between target and num
    Once the difference is found, check if the difference exists in a hashmap of numbers and their index.
    If the difference is not found, the num and its index can be added to the hashmap. 
        Time Complexity: O(n)
        Space Complexity: O(n)

    Sorting - 
    Sort the array of integers first and then compute the difference to look for, for each number in the sorted array.
    Since the array is sorted, a binary search can be used to search for the difference. 
        Time Complexity: O(nlogn)
        Space Complexity: O(n)/O(1)... depends on the sorting algorithm
    """

    # Go through every num in the nums list and check for the difference between target and num
    # Once the difference is found, check if the difference exists in a hashmap of numbers and their index.
    # If the difference is not found, the num and its index can be added to the hashmap. 
    numIndices = {}

    for i in range(len(nums)): 
        difference = target - nums[i]
        if numIndices.get(difference) != None: 
            return [numIndices[difference], i]
        numIndices[nums[i]] = i

print("Result:", twoSum([2, 15, 21, 9, 6, 7], 9))    