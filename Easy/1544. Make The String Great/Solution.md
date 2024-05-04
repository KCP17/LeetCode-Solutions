## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/b09991ca-fb95-4c76-9b97-d3da3a2595a9)

## Code (Python3)
```python3 []
class Solution:
    def makeGood(self, s: str) -> str: # Stack
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32: # Refer to ASCII table: |lower_of_same_char - upper_of_same_char| = 32
                stack.pop() # Pop the lower (upper) off top of stack whenever we see its upper (lower) version
            else:
                stack.append(c)
        return "".join(stack)
```
## Note:
Stack (My solution):
- Time: $$O(N)$$
- Space: $$O(N)$$
