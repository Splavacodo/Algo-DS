def searchMatrix(matrix: list[list[int]], target: int) -> bool: 
    """
    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.
    """
    # Perform a binary search on the rows and check the first number in the row. The first
    # number in the row should be less than or equal to the number being searched for.
    leftRowPtr = 0
    rightRowPtr = len(matrix) - 1
    while leftRowPtr <= rightRowPtr: 
        middleRowPtr = int((leftRowPtr + rightRowPtr)/2)

        if matrix[middleRowPtr][0] == target: 
            return True
        elif matrix[middleRowPtr][0] > target: 
            rightRowPtr = middleRowPtr - 1
        else: 
            # At this point it's possible for this row to contain the target
            leftColPtr = 0
            rightColPtr = len(matrix[middleRowPtr]) - 1

            while leftColPtr <= rightColPtr: 
                middleColPtr = int((leftColPtr + rightColPtr)/2)

                if matrix[middleRowPtr][middleColPtr] == target: 
                    return True 
                elif matrix[middleRowPtr][middleColPtr] > target: 
                    rightColPtr = middleColPtr - 1
                else: 
                    leftColPtr = middleColPtr + 1
            
            leftRowPtr = middleRowPtr + 1
    
    return False 

print("Result:", searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))