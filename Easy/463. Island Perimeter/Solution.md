## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/e7be2e07-7ed2-49be-bb91-3e9b5006f872)

## Code (Python3)
```python3 []
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
```
## Note:
Logic (My solution):
- Time: $$O(ROWS * COLS)$$
- Space: $$O(1)$$
