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
