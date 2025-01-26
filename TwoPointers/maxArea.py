def maxArea(height: list[int]) -> int: 
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
    of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.
    """
    # To find the maximum area, compute the area between two pointers. One pointer will start at the beginning of 
    # the input list, the other will start at the end of the input list. 

    # The area will be computed by the following equation: A = (rightPtr - leftPtr) * min(height[leftPtr], heightRightPtr)
    
    # Which pointer should be moved? The one with a lower height
    leftPtr = 0
    rightPtr = len(height) - 1
    maxArea = 0 

    while leftPtr < rightPtr: 
        currArea = (rightPtr - leftPtr) * min(height[leftPtr], height[rightPtr])
        if currArea > maxArea: 
            maxArea = currArea
        
        if height[leftPtr] < height[rightPtr]: 
            leftPtr += 1
        else: 
            rightPtr -= 1
    
    return maxArea 

print("Result:", maxArea([1,8,6,2,5,4,8,3,7]))