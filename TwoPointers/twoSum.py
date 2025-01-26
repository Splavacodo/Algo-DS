def twoSum(nums: list[int], target: int) -> list[int]: 
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find 
    two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
    and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array 
    [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.
    """
    # Check if there's only two numbers in the array or if the first two numbers add up to the target
    if len(nums) == 2 or nums[0] + nums[1] == target: 
        return [1, 2]

    # Have two pointers that start at different points in the list, one at the beginning and the other at the end
    # If the number at the right pointer is greater than target, the right pointer should move
    # If the sum of both numbers at each pointer are greater than the sum, the right pointer should move
    # If the sum of both numbers at each pointer is less then the sum, the left pointer should move
    leftPtr = 0
    rightPtr = len(nums) - 1
    tempSum = nums[leftPtr] + nums[rightPtr]

    # Need a while loop, don't know how many times to move each pointer
    while leftPtr < rightPtr and tempSum != target: 
        tempSum = nums[leftPtr] + nums[rightPtr]
        if tempSum > target: 
            rightPtr -= 1
        elif tempSum < target: 
            leftPtr += 1
    
    return [leftPtr + 1, rightPtr + 1]

print("Result:", twoSum([-10,-8,-2,1,2,5,6], 0))        