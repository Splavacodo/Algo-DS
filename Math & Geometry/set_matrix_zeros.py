class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_to_modify = set()
        cols_to_modify = set()

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rows_to_modify.add(row)
                    cols_to_modify.add(col)
        
        for row in rows_to_modify:
            for col in range(cols):
                matrix[row][col] = 0
        
        for col in cols_to_modify:
            for row in range(rows):
                matrix[row][col] = 0
        