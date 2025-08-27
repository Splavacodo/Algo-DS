class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []

        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            
            top += 1

            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            
            right -= 1

            if not left <= right or not top <= bottom:
                break
            
            for col in range(right, left - 1, -1):
                spiral.append(matrix[bottom][col])
            
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                spiral.append(matrix[row][left])
            
            left += 1
        
        return spiral
    