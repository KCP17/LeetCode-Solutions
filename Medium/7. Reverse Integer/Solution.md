## 1. Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/aa8714a4-9101-4272-bc6a-a5d1db5385ef)

## 2. Code (Python3)
### 2.1. Most readable
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
### 2.2. Two lines
```python3 []
class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        return res if -2**31 <= res <= 2**31 else 0
```
### 2.3. One line
```python3 []
class Solution:
    def reverse(self, x: int) -> int:
        return int(str(abs(x))[::-1]) * (1 if x >= 0 else -1) if -2**31 <= int(str(abs(x))[::-1]) * (1 if x >= 0 else -1) <= 2**31 else 0
```
## 3. Time & Space (for all 3 solutions above)
* Time: $$O(N)$$
* Space: $$O(N)$$
