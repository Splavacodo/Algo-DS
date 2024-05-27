def threeSum(nums: list[int]) -> list[list[int]]: 
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
    i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Approach: 
    To find all the possible combinations of sums, the array can be sorted first. Each number in
    the input list will be looped over and there will be two additional pointers that will search
    for numbers that sum to zero. This requires having to go through every other number while not
    including duplicates. 
        - Time Complexity: O(n^2)
        - Space Complexity: O(n)
    """
    # Before starting, sort the array so it can be clear which pointer should be moved
    nums.sort()

    sumToZero = []
    # Have two pointers, one that starts at in front of the current val and the 
    # another that starts at the end of the list
    for i, currNum in enumerate(nums): 
        # Check if the neighbor of the current number is the same to avoid duplicate
        # solutions
        if i > 0 and currNum == nums[i - 1]: 
            continue

        leftPtr, rightPtr = i + 1, len(nums) - 1

        while leftPtr < rightPtr:
            currSum = currNum + nums[leftPtr] + nums[rightPtr]

            if currSum < 0: 
                leftPtr += 1
            elif currSum > 0: 
                rightPtr -= 1
            elif currSum == 0:
                sumToZero.append([currNum, nums[leftPtr], nums[rightPtr]])
                leftPtr += 1
                while nums[leftPtr] == nums[leftPtr - 1] and leftPtr < rightPtr:
                    leftPtr += 1

    return sumToZero 

print("Result:", threeSum([-1,0,1,2,-1,-4]))