## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/3d8db058-a26b-43c1-a688-02bbb1a8ba78)

## Code (Python3)
```python3 []
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.truediv}
        
        for sym in tokens:
            if sym not in operators:
                stack.append(int(sym))
            else:
                right_oprd = stack.pop()
                left_oprd = stack.pop()
                stack.append(int(operators[sym](left_oprd, right_oprd)))

        return stack[-1]
```
## Note:
Stack (My solution):
- Time: $$O(N)$$
- Space: $$O(N)$$
