class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += 1 if grid[r][c] == 1 and (grid[r - 1][c] if r - 1 >= 0 else 0) == 0 else 0
                res += 1 if grid[r][c] == 1 and (grid[r + 1][c] if r + 1 < ROWS else 0) == 0 else 0
                res += 1 if grid[r][c] == 1 and (grid[r][c - 1] if c - 1 >= 0 else 0) == 0 else 0
                res += 1 if grid[r][c] == 1 and (grid[r][c + 1] if c + 1 < COLS else 0) == 0 else 0
        return res
