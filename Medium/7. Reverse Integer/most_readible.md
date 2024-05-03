## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/1c1a2f2f-ae8c-46d0-9c63-8fbeafeae764)
## Code (Python3)
```python3 []
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x_reversed = int(''.join(reversed(x[1:])))
            return -x_reversed if -x_reversed >= -2**31 else 0
        else:
            x_reversed = int(''.join(reversed(x)))
            return x_reversed if x_reversed <= 2**31 else 0
```
