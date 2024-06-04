## Efficiency
![image](https://github.com/KCP17/LeetCode-Solutions/assets/148914885/b1e14d6e-3333-4c92-9544-679689928cd0)

## Code (Python3)
```python3 []
class Solution:
    def longestPalindrome(self, s: str) -> int:
        sum_even, odd = 0, False
        for freq in Counter(s).values():
            if freq % 2 == 0:
                sum_even += freq
            else:
                odd = True
                sum_even += (freq - 1)
        return sum_even + 1 if odd else sum_even
```
## Time & Space:
Counting (My solution):
* Time: $$O(2N)$$
* Space: $$O(N)$$
