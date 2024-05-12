## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/1aba9a4a-14ac-44b4-8c22-45bcf909ed9d)

## Code (Python3)
```python3 []
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(grid)
        
        for R in range(n - 2):
            res.append([])
            for C in range(n - 2):
                max_val = 0
                for r in range(R, R + 3):
                    for c in range(C, C + 3):
                        max_val = max(max_val, grid[r][c])
                
                res[-1].append(max_val)

        return res
```
## Note:
Brute force (My solution):
- Time: $$O( 3 * 3 * (n-2)^2 )$$
- Space: $$O(1)$$
