class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def find_word(loc, word_idx):
            x_loc = loc[0]
            y_loc = loc[1]

            if word_idx == len(word):
                return True
            elif (not 0 <= x_loc < rows or 
                  not 0 <= y_loc < cols or 
                  loc in visited or 
                  board[x_loc][y_loc] != word[word_idx]):
                return False
            
            visited.add(loc)
            found = (find_word((x_loc - 1, y_loc), word_idx + 1) or
                    find_word((x_loc + 1, y_loc), word_idx + 1) or
                    find_word((x_loc, y_loc - 1), word_idx + 1) or
                    find_word((x_loc, y_loc + 1), word_idx + 1))
            visited.remove(loc)

            return found
        
       
        for row in range(rows):
            for col in range(cols):
                if find_word((row, col), 0):
                    return True
        
        return False