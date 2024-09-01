## 1. Efficiency (Python3)
![image](https://github.com/user-attachments/assets/0e9adb51-5812-462c-bf62-cd8b13ffebe3)

## 2. Code (Python3)
```python3 []
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n: return []
        res = []
        prev = 0
        for r in range(m):
            res.append(original[prev : prev + n])
            prev += n
        return res
```

## 3. Note
My solution:
- Time: $$O(m*n)$$
- Space: $$O(m*n)$$
