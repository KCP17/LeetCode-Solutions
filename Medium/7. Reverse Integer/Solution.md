## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/aa8714a4-9101-4272-bc6a-a5d1db5385ef)

## Code (Python3)
```python3 []
class Solution:
    def reverse(self, x: int) -> int:
        return int(str(abs(x))[::-1]) * (1 if x >= 0 else -1) if -2**31 <= int(str(abs(x))[::-1]) * (1 if x >= 0 else -1) <= 2**31 else 0
```
## Time & Space
* Time: $$O(N)$$
* Space: $$O(N)$$
