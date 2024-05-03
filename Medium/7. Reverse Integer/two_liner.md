## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/11e801ef-3c75-4a6b-8b60-0c4fbd4eccf5)

## Code (Python3)
```python3 []
class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        return res if -2**31 <= res <= 2**31 else 0
```
