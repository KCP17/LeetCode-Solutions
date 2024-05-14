class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited or grid[r][c] == 0: # Invalid cell
                return 0
            visited.add((r, c)) # Mark as visited

            # Always choose the max out of 4 sub-paths
            search = max(
                            dfs(r - 1, c), # Up
                            dfs(r + 1, c), # Down
                            dfs(r, c - 1), # Left
                            dfs(r, c + 1) # Right
                        )
            
            visited.remove((r, c)) # Backtracking
            
            return grid[r][c] + search # Accumulate the current cell's value with the max searched sub-path

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                visited = set() # Starting a new path with no visited cells yet
                res = max(res, dfs(row, col)) # Choose the max-valued path

        return res
