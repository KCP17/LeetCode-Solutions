## Efficiency
![image](https://github.com/KCP17/Leetcode-solutions/assets/148914885/79c0440c-7190-444f-810c-97806eb2f330)

## Code (Python3)
```python3 []
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_mapto_t, t_mapto_s = {}, {}
        for i in range(len(s)):
            # If s[i] is already existed AND its corresponding t[i] is DIFFERENT from the t[i] that it previously mapped to, OR vice versa --> NOT Isomorphic
            if (s[i] in s_mapto_t and t[i] != s_mapto_t[s[i]]) or (t[i] in t_mapto_s and s[i] != t_mapto_s[t[i]]):
                return False
            s_mapto_t[s[i]] = t[i] # Map s[i] to its corresponding t[i]
            t_mapto_s[t[i]] = s[i] # Map t[i] to its corresponding s[i]
        return True
```

## Time & Space:
* Time: $$O(N)$$
* Space: $$O(2N)$$ worst case
