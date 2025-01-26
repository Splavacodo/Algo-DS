def binarySearch(nums: list[int], target: int) -> int: 
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target, 
    write a function to search target in nums. If target exists, then return its index. 
    Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    """
    leftPtr = 0
    rightPtr = len(nums) - 1

    while leftPtr <= rightPtr: 
        middlePtr = int((leftPtr + rightPtr) / 2)

        if nums[middlePtr] == target: 
            return middlePtr
        elif nums[middlePtr] < target: 
            leftPtr = middlePtr + 1
        else: 
            rightPtr = middlePtr - 1
        
    
    return -1

print("Result:", binarySearch([2, 4, 6, 8, 10], 10))