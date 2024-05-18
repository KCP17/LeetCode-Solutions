## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/82e00b51-a088-4356-bf8f-753ff370db7e)

## Code (Python)
```python []
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_ones = s.count('1')
        # Maximize by putting as many adjacent '1's as possible at the beginning of the binary number, LSB is always '1' to indicate an odd number
        return '1' * (count_ones - 1) + '0' * (len(s) - count_ones) + '1'
```
## Note:
My optimized solution:
- Time: $$O(2n)$$
- Space: $$O(n)$$
