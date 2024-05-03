## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/2cf0e685-d9c9-44a9-ad6e-98cbe18ec8a8)

## Code (Python3)
```python3 []
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] == 'I':
                res += 1
                if i+1 < len(s):
                    if s[i+1] == 'V' or s[i+1] == 'X': res -=2
            elif s[i] == 'V': res += 5
            elif s[i] == 'X':
                res += 10
                if i+1 < len(s):
                    if s[i+1] == 'L' or s[i+1] == 'C': res -=20
            elif s[i] == 'L': res += 50
            elif s[i] == 'C':
                res += 100
                if i+1 < len(s):
                    if s[i+1] == 'D' or s[i+1] == 'M': res -=200
            elif s[i] == 'D': res += 500
            else: res += 1000
        return res
```
## Time & Space:
* Time: $$O(n)$$
* Space: $$O(1)$$
