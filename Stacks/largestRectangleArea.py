def largestRectangleArea(heights: list[int]) -> int: 
    """
    Given an array of integers heights representing the histogram's bar height where the width 
    of each bar is 1, return the area of the largest rectangle in the histogram.
    """
    largestArea = 0
    heightStack = [] # the stack will contain a pair that contains the index and height

    for i, h in enumerate(heights): 
        # Storing the start index will be useful for computing intermediate areas
        start = i 

        while heightStack and heightStack[-1][1] > h:
            heightIdx, height = heightStack.pop() 
            largestArea = max(largestArea, height * (i - heightIdx))
            start = heightIdx 

        heightStack.append((start, h))

    for i, h in heightStack: 
        largestArea = max(largestArea, h * (len(heights) - i))
    
    return largestArea

print("Result:", largestRectangleArea([2,1,5,6,2,3]))