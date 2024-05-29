## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/bdf18097-7b2e-44be-8012-6246d4d2a5e4)

## Code (Python3)
```python3 []
class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        num = int(s, 2) # Convert binary (base 2) to decimal
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            res += 1
        return res
```
## Note:
Converting - little bit of cheating (My solution):
- Time: $$O(n + log2(n))$$
- Space: $$O(1)$$
