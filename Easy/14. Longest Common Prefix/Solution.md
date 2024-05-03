## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/e4cf15c7-2abb-418e-8dde-878bf3a2afa1)

## Code (Python3)
```python3 []
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        output = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if (strs[j][i] if i < len(strs[j]) else "") != strs[0][i]:
                    return output

                if j == len(strs) - 1:
                    output += strs[j][i]
        return output
```
## Time & Space:
* Time: $$O(M*N)$$ with M is length of 1st substring, N is length of `strs`
* Space: $$O(M)$$
