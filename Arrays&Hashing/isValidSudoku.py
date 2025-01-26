from collections import defaultdict

def isValidSudoku(board: list[list[str]]) -> bool: 
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:
        - A Sudoku board (partially filled) could be valid but is not necessarily solvable.

        - Only the filled cells need to be validated according to the mentioned rules.
    """
    # Create a empty hashmap and iterate through each row in the board
    # After a single row has been checked, clear the map and proceed to the next row
    validation = set()

    for row in board: 
        for num in row: 
            if num == ".": 
                continue
            elif num in validation: 
                return False
            else: 
                validation.add(num)
        validation.clear()

    # After each row has been verified, check each column using a similar approach
    for col in range(len(board)): 
        for row in range(len(board)): 
            if board[row][col] == ".": 
                continue
            elif board[row][col] in validation: 
                return False
            validation.add(board[row][col])
        validation.clear()

    # The final step is to find a way identify each 3x3 grid in the board and the numbers in each grid
    # One approach is to use a default dictionary with a set as a value in the dictionary
    gridValidation = defaultdict(set)

    for row in range(len(board)): 
        for col in range(len(board)):
            if(board[row][col] == "."): 
                continue
            if(board[row][col] in gridValidation[(row//3, col//3)]): 
                return False 
            gridValidation[(row//3, col//3)].add(board[row][col])
    
    return True 
            
board = [
["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print("Result:", isValidSudoku(board))