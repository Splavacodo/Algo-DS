# def num_increasing_paths(grid) -> int:
#     rows = len(grid)
#     cols = len(grid[0])

#     memo_table = [[-1 for _ in range(cols)] for _ in range(rows)]

#     def dfs(row, col):
#         if memo_table[row][col] != -1:
#             return memo_table[row][col]
        
#         count = 1

#         for new_row, new_col in [(row, col - 1), (row - 1, col), (row, col + 1), (row + 1, col)]:
#             if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] > grid[row][col]:
#                 count += dfs(new_row, new_col)
    
#         if count > 1:
#             memo_table[row][col] = count - 1

#         return count

#     total_paths = 0

#     for row in range(rows):
#         for col in range(cols):
#             total_paths += dfs(row, col)
    
#     return total_paths

# grid1 = [
#     [1, 2],
#     [3, 4]
# ]

# print(num_increasing_paths(grid1))
def num_increasing_paths(grid) -> int:
    if not grid or not grid[0]:
        return 0
        
    rows = len(grid)
    cols = len(grid[0])
    
    memo = {}
    
    def dfs(row, col, prev_val, path_length):
        # Base cases
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] <= prev_val:
            return 0
            
        # Check if result is already memoized
        if (row, col, prev_val, path_length) in memo:
            return memo[(row, col, prev_val, path_length)]
        
        # Directions: up, right, down, left
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        paths = 1 if path_length >= 1 else 0  # Only count if path length is at least 2
        
        # Try all directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            paths += dfs(new_row, new_col, grid[row][col], path_length + 1)
            
        memo[(row, col, prev_val, path_length)] = paths
        return paths
    
    total_paths = 0
    # Start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            total_paths = total_paths + dfs(i, j, -1, 0)
            
    return total_paths

# Test cases
grid1 = [
    [1, 2],
    [3, 4]
]

print(num_increasing_paths(grid1))  # Should print: 6