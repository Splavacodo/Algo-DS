def trap(height: list[int]) -> int: 
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1, 
    compute how much water it can trap after raining.
    """
    # Check if the input array has less than two items, the water trapped will always be zero for this case
    if len(height) < 2: 
        return 0
    
    # Create two pointers, one at the beginning of the input list and the other at the end of
    # the input list
    leftPtr = 0
    rightPtr = len(height) - 1

    # The left pointer will keep track of the max height on the left side of the list
    # The right pointer will keep track of the max height on the right side of the list
    maxL = height[leftPtr]
    maxR = height[rightPtr]

    totalTrapped = 0

    while leftPtr < rightPtr: 
        if maxL < maxR: 
            leftPtr += 1
            maxL = max(maxL, height[leftPtr])
            totalTrapped += maxL - height[leftPtr]
        else: 
            rightPtr -= 1 
            maxR = max(maxR, height[rightPtr])
            totalTrapped += maxR - height[rightPtr]
    
    return totalTrapped 

print("Result:", trap([0,1,0,2,1,0,1,3,2,1,2,1]))