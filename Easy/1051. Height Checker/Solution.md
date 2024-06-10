## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/eaffa6b2-b90f-4039-b494-a84260404d5b)

## Code (Python3)
```python3 []
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
```
## Note:
Normal Sorting (My solution):
- Time: $$O(n + n*log(n))$$
- Space: $$O(n)$$
