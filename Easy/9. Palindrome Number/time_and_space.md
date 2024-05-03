## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/7fa5d604-c764-4ab3-b16f-d3499c731267)
## Code (Python3)
```python3 []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return True if x == ''.join(reversed(x)) else False
```
## TIme & Space:
* Time: $$O(n)$$
* Space: $$O(n)$$
