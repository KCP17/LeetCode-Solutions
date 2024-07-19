## 1. Efficiency (Python3)
![image](https://github.com/user-attachments/assets/6a29083c-3335-4477-8870-dbb996fdfd27)

## 2. Code (Python3)
```python3 []
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        valid_nums = set()
        res = []
        for r in range(ROWS):
            valid_nums.add(min(matrix[r]))
        
        for c in range(COLS):
            col_max = 0
            for r in range(ROWS):
                if matrix[r][c] > col_max:
                    col_max = matrix[r][c]
            if col_max in valid_nums:
                res.append(col_max)
        return res
```

## 3. Note:
HashSet (My solution):
- Time: $$O(2 * N * M)$$
- Space: $$O(N)$$
