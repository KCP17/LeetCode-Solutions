## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/ccef785c-7d9f-4c5f-8f7f-c838fe1f6d59)

## Code (Python3)
```python3 []
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if stack and ((p == ')' and stack[-1] == '(') or (p == ']' and stack[-1] == '[') or (p == '}' and stack[-1] == '{')):
                stack.pop()
            else:
                stack.append(p)
        
        return True if not stack else False
```
## Time & Space:
* Time: $$O(N)$$
* Space: $$O(N)$$
